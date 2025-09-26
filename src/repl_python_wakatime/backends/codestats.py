"""Codestats
============

Refer `code-stats-vim
<https://gitlab.com/code-stats/code-stats-vim/-/blob/master/pythonx/codestats.py>
`_.
"""

import asyncio
import json
import logging
from dataclasses import dataclass
from datetime import datetime
from socket import gethostname
from threading import Thread
from time import time

from aiohttp import ClientSession
from aiohttp.client import ClientTimeout
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
    url: str = "https://codestats.net/api/my/pulses/"
    interval: int = 60  # interval at which stats are sent
    timeout: ClientTimeout | None = None

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
        self.data = {
            "coded_at": "",
            "xps": [{"language": self.language_type, "xp": 0}],
        }
        self.datetime = datetime.now().astimezone()
        if self.timeout is None:
            self.timeout = ClientTimeout(10)
        self.session = None

    def __call__(self, xp: int = 1) -> None:
        """Add xp.

        Sem sections are super small so this should be quick if it blocks.

        :param xp:
        :type xp: int
        :rtype: None
        """
        self.data["xps"][0]["xp"] += xp
        if (
            time() - self.datetime.timestamp() > self.interval
            and self.data["xps"][0]["xp"] > 0
        ):
            co = self.send_xp()
            Thread(target=asyncio.run, args=(co,)).run()

    async def send_xp(self) -> str:
        """Send xp.

        :rtype: str
        """
        self.datetime = datetime.now().astimezone()
        self.data["coded_at"] = self.datetime.isoformat()
        data = json.dumps(self.data).encode("utf-8")
        text = ""
        if self.session is None:
            self.session = ClientSession(
                base_url=self.url,
                headers=self.headers,
                timeout=self.timeout,
            )
        try:
            async with self.session.post(
                "/",
                data=data,
            ) as resp:
                text = await resp.text()
            self.data["xps"][0]["xp"] = 0
        except TimeoutError as error:
            logger.error(error)
        return text
