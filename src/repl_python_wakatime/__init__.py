"""Refer `create-plugin <https://wakatime.com/help/creating-plugin>`_."""
import logging
import os
from shutil import which
from subprocess import run  # nosec: B404
from threading import Thread
from typing import Any, Callable

try:
    from ._version import __version__, __version_tuple__  # type: ignore
except ImportError:
    __version__ = "rolling"
    __version_tuple__ = (0, 0, 0, __version__, "")

logger = logging.getLogger(__name__)


def send_wakatime_heartbeat(
    project: str = "",
    category: str = "coding",
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
    :param category:
    :type category: str
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
            f"--category={category}",
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
    task = Thread(target=send_wakatime_heartbeat, args=args, kwargs=kwargs)
    task.daemon = True
    task.start()
