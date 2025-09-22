"""Codestats
============

Refer `code-stats-vim
<https://gitlab.com/code-stats/code-stats-vim/-/blob/master/pythonx/codestats.py>
`_.
"""

import json
import logging
import threading
from dataclasses import dataclass
from datetime import datetime
from http.client import HTTPException
from socket import gethostname
from ssl import CertificateError
from time import sleep
from typing import NoReturn
from urllib.error import URLError
from urllib.request import Request, urlopen

from keyring import get_keyring
from keyring.errors import NoKeyringError

from .. import __version__
from . import Hook

logger = logging.getLogger(__name__)


@dataclass
class CodeStats(Hook):
    """Codestats."""

    service_name: str = "codestats"
    user_name: str = gethostname()
    url: str = "https://codestats.net/api/my/pulses"
    interval: int = 10  # interval at which stats are sent
    sleep_interval: float = 0.1  # sleep interval for timeslicing
    timeout: int = 2  # request timeout value (in seconds)

    def __post_init__(
        self,
    ) -> None:
        """Init.

        :rtype: None
        """
        keyring = get_keyring()
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": f"{self.plugin}/{__version__}",
            "X-API-Token": keyring.get_password(
                self.service_name, self.user_name
            ),
            "Accept": "*/*",
        }
        if not self.headers["X-API-Token"]:
            raise NoKeyringError

        self.xp_dict = {self.language_type: 0}
        self.sem = threading.Semaphore()
        self.thread = threading.Thread(target=self.run, daemon=True)
        self.thread.start()

    def __call__(self, xp: int = 1) -> None:
        """Add xp.

        Sem sections are super small so this should be quick if it blocks.

        :param xp:
        :type xp: int
        :rtype: None
        """
        self.sem.acquire()
        self.xp_dict[self.language_type] += xp
        self.sem.release()

    def send_xp(self) -> None:
        """Send xp.

        Acquire the lock to get the list of xp to send.

        :rtype: None
        """
        if len(self.xp_dict) == 0:
            return

        self.sem.acquire()
        xp_list = [
            {"language": ft, "xp": xp} for ft, xp in self.xp_dict.items()
        ]
        self.xp_dict = {self.language_type: 0}
        self.sem.release()

        # after lock is released we can send the payload
        utc_now = datetime.now().astimezone().isoformat()
        data = json.dumps({
            "coded_at": f"{utc_now}",
            "xps": xp_list,
        }).encode("utf-8")
        req = Request(url=self.url, data=data, headers=self.headers)
        error = ""
        try:
            response = urlopen(req, timeout=self.timeout)
            response.read()
            # connection might not be closed without .read()
        except URLError as e:
            try:
                # HTTP error
                error = "{} {}".format(
                    e.code,  # type: ignore
                    e.read().decode("utf-8"),  # type: ignore
                )
            except AttributeError:
                # non-HTTP error, eg. no network
                error = e.reason
        except HTTPException as e:
            error = f"HTTPException on send data. \nDoc: {e.__doc__}"
        except (CertificateError, TimeoutError) as e:
            # SSL certificate error (eg. a public wifi redirects traffic)
            error = e
        if error:
            logger.error(error)

    def run(self) -> NoReturn:
        """Run main thread.

        Needs to be able to send XP at an interval.

        :param self:
        :rtype: NoReturn
        """
        while True:
            cur_time = 0
            while cur_time < self.interval:
                sleep(self.sleep_interval)
                cur_time += self.sleep_interval

            self.send_xp()
