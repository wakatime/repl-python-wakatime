"""Refer `create-plugin <https://wakatime.com/help/creating-plugin>`_."""
import logging
import os
from shutil import which
from subprocess import run  # nosec: B404
from threading import Thread
from typing import Any, Callable

from ._version import __version__, __version_tuple__  # type: ignore

logger = logging.getLogger(__name__)


def send_wakatime_heartbeat(
    project: str = "",
    plugin: str = "repl-python-wakatime",
    filenames: list[str] = [".git"],
    detect_func: Callable[[str], bool] = os.path.isdir,
) -> None:
    """Send wakatime heartbeat.

    If ``project == ""``, detect automatically.

    ``plugin`` must be the format of ``repl-REPL_NAME-wakatime`` to let
    wakatime detect correctly.

    :param project:
    :type project: str
    :param plugin:
    :type plugin: str
    :param filenames:
    :type filenames: list[str]
    :param detect_func:
    :type detect_func: Callable[[str], bool]
    :rtype: None
    """
    if project == "":
        from .utils import get_project

        project = get_project(filenames, detect_func)
    run(  # nosec: B603 B607
        [
            "wakatime-cli",
            "--write",
            f"--plugin={plugin}",
            "--entity-type=app",
            "--entity=python",
            "--alternate-language=python",
            f"--project={project}",
        ],
        stdout=open(os.devnull, "w"),
    )


def wakatime_hook(*args: Any, **kwargs: Any) -> None:
    """Wakatime hook.

    :param args:
    :type args: Any
    :param kwargs:
    :type kwargs: Any
    :rtype: None
    """
    if which("wakatime-cli") is None:
        logger.error("Please install wakatime-cli firstly!")
        return
    task = Thread(target=send_wakatime_heartbeat, args=args, kwargs=kwargs)
    task.daemon = True
    task.start()
