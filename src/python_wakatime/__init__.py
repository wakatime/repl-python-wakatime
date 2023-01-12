"""Wakatime
===========

`create-plugin <https://wakatime.com/help/creating-plugin>`_
"""
import os
from subprocess import run  # nosec: B404
from threading import Thread
from typing import Any

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


def wakatime_hook(args: tuple = (), kwargs: dict[str, Any] = {}) -> None:
    """Wakatime hook.

    :param args:
    :type args: tuple
    :rtype: None
    """
    task = Thread(target=send_wakatime_heartbeat, args=args, kwargs=kwargs)
    task.daemon = True
    task.start()
