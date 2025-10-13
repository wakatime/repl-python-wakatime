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
from threading import Event, Lock, Thread
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

    def __post_init__(self) -> None:
        """Init.

        :rtype: None
        """
        keyring = get_keyring()
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": f"{self.plugin}/{__version__}",
            "X-API-Token": keyring.get_password(self.service_name, self.user_name),
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
        self.loop = asyncio.new_event_loop()
        self.event = Event()
        self.lock = Lock()
        self.thread = Thread(target=self.worker, daemon=True)
        self.thread.start()

    def __call__(self, xp: int = 1) -> None:
        """Add xp.

        Sem sections are super small so this should be quick if it blocks.

        :param xp:
        :type xp: int
        :rtype: None
        """
        with self.lock:
            self.data["xps"][0]["xp"] += xp
        if time() - self.datetime.timestamp() > self.interval:
            self.event.set()

    def worker(self) -> None:
        """Worker.

        :param self:
        :rtype: None
        """
        asyncio.set_event_loop(self.loop)
        while True:
            self.event.wait()
            self.loop.run_until_complete(self.send_xp())
            self.event.clear()

    def __del__(self) -> None:
        if self.session:
            self.loop.run_until_complete(self.session.close())
        self.loop.close()

    async def send_xp(self) -> str:
        """Send xp.

        :rtype: str
        """
        if self.session is None:
            self.session = ClientSession(
                base_url=self.url,
                headers=self.headers,
                timeout=self.timeout,
            )
        self.datetime = datetime.now().astimezone()
        self.data["coded_at"] = self.datetime.isoformat()
        text = ""
        with self.lock:
            data = json.dumps(self.data).encode("utf-8")
            xp = self.data["xps"][0]["xp"]
        try:
            async with self.session.post(
                "/",
                data=data,
            ) as resp:
                text = await resp.text()
            with self.lock:
                self.data["xps"][0]["xp"] -= xp
        except TimeoutError as error:
            logger.error(error)
        return text
