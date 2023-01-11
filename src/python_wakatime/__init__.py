"""Wakatime
===========

`create-plugin <https://wakatime.com/help/creating-plugin>`_
"""
import os
import sys
from subprocess import run  # nosec: B404
from threading import Thread
from typing import Callable

from ._version import __version__, __version_tuple__  # type: ignore


def send_wakatime_heartbeat(project: str = "Terminal") -> None:
    """Send wakatime heartbeat.

    :param project:
    :type project: str
    :rtype: None
    """
    run(  # nosec: B603 B607
        [
            "wakatime-cli",
            "--write",
            "--plugin=python-wakatime",
            "--entity-type=app",
            "--entity=python",
            "--alternate-language=python",
            f"--project={project}",
        ],
        stdout=open(os.devnull, "w"),
    )


def wakatime_hook(args: tuple = ()) -> None:
    """Wakatime hook.

    :param args:
    :type args: tuple
    :rtype: None
    """
    task = Thread(target=send_wakatime_heartbeat, args=args)
    task.daemon = True
    task.start()


class Ps1:
    """Ps1."""

    def __init__(
        self,
        ps1: object = None,
        hook: Callable = wakatime_hook,
        args: tuple = (),
    ) -> None:
        """Init.

        :param ps1:
        :type ps1: object
        :param hook:
        :type hook: Callable
        :param args:
        :type args: tuple
        :rtype: None
        """
        if ps1:
            self.ps1 = ps1
        else:
            if hasattr(sys, "ps1"):
                self.ps1 = sys.ps1
            else:
                self.ps1 = ">>> "
        self.args = args
        self.hook = hook

    def __str__(self) -> str:
        """Str.

        :rtype: str
        """
        self.hook(*self.args)
        if isinstance(self.ps1, str):
            return self.ps1
        else:
            return str(self.ps1)


def install_hook(hook: Callable = wakatime_hook, args: tuple = ()) -> None:
    """Install hook. Only install once.

    :param hook:
    :type hook: Callable
    :param args:
    :type args: tuple
    :rtype: None
    """
    if hasattr(sys, "ps1") and isinstance(sys.ps1, Ps1):
        return
    sys.ps1 = Ps1(hook=hook, args=args)
