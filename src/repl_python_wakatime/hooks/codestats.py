"""Codestats
============

Refer `code-stats-vim
<https://gitlab.com/code-stats/code-stats-vim/-/blob/master/pythonx/codestats.py>
`_.
"""

import json
import logging
import threading
import time
from datetime import datetime
from http.client import HTTPException
from socket import gethostname
from ssl import CertificateError
from typing import Any, NoReturn
from urllib.error import URLError
from urllib.request import Request, urlopen

from .. import __version__

logger = logging.getLogger(__name__)
INTERVAL = 10  # interval at which stats are sent
SLEEP_INTERVAL = 0.1  # sleep interval for timeslicing
TIMEOUT = 2  # request timeout value (in seconds)

codestats = None


def codestats_hook(
    api_key: str = "",
    url: str = "https://codestats.net/api/my/pulses",
    language: str = "python",
    language_type: str = "Terminal (%s)",
    service_name: str = "codestats",
    user_name: str = gethostname(),
    *args: Any,
    **kwargs: Any,
) -> None:
    """Codestats hook.

    :param api_key:
    :type api_key: str
    :param url:
    :type url: str
    :param language:
    :type language: str
    :param language_type:
    :type language_type: str
    :param service_name:
    :type service_name: str
    :param user_name:
    :type user_name: str
    :param args:
    :type args: Any
    :param kwargs:
    :type kwargs: Any
    :rtype: None
    """
    global codestats
    if codestats is None:
        if api_key == "":
            from ..utils.api import get_api_key

            api_key = get_api_key(service_name, user_name)
        codestats = CodeStats(api_key, url, language_type % language)
    codestats.add_xp()


class CodeStats:
    """Codestats."""

    def __init__(
        self,
        api_key: str,
        url: str = "https://codestats.net/api/my/pulses",
        language_type: str = "Terminal (python)",
    ) -> None:
        """Init.

        :param api_key:
        :type api_key: str
        :param url:
        :type url: str
        :param language:
        :type language: str
        :param language_type:
        :type language_type: str
        :rtype: None
        """
        self.url = url
        self.api_key = api_key
        self.language_type = language_type
        self.xp_dict = {language_type: 0}

        self.sem = threading.Semaphore()

        self.cs_thread = threading.Thread(target=self.main_thread)
        self.cs_thread.daemon = True
        self.cs_thread.start()

    def add_xp(self, xp: int = 1) -> None:
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
        xp_list = [dict(language=ft, xp=xp) for ft, xp in self.xp_dict.items()]
        self.xp_dict = {self.language_type: 0}
        self.sem.release()

        headers = {
            "Content-Type": "application/json",
            "User-Agent": f"code-stats-python/{__version__}",
            "X-API-Token": self.api_key,
            "Accept": "*/*",
        }

        # after lock is released we can send the payload
        utc_now = datetime.now().astimezone().isoformat()
        pulse_json = json.dumps({
            "coded_at": f"{utc_now}",
            "xps": xp_list,
        }).encode("utf-8")
        req = Request(url=self.url, data=pulse_json, headers=headers)
        error = ""
        try:
            response = urlopen(req, timeout=TIMEOUT)  # nosec: B310
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
        except CertificateError as e:
            # SSL certificate error (eg. a public wifi redirects traffic)
            error = e
        except HTTPException as e:
            error = f"HTTPException on send data. \nDoc: {e.__doc__}"
        if error:
            logger.error(error)

    def main_thread(self) -> NoReturn:
        """Run main thread.

        Needs to be able to send XP at an interval.
        """
        while True:
            cur_time = 0
            while cur_time < INTERVAL:
                time.sleep(SLEEP_INTERVAL)
                cur_time += SLEEP_INTERVAL

            self.send_xp()
