"""Wakatime
===========

Refer `create-plugin <https://wakatime.com/help/creating-plugin>`_.
"""
import os
from subprocess import Popen  # nosec: B404
from typing import Any, Callable


def wakatime_hook(
    project: str = "",
    category: str = "coding",
    plugin: str = "repl-python-wakatime",
    filenames: list[str] = [".git"],
    detect_func: Callable[[str], bool] = os.path.isdir,
    *args: Any,
    **kwargs: Any,
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
        from ..utils.project import get_project

        project = get_project(filenames, detect_func)
    Popen(  # nosec: B603 B607
        [
            "wakatime-cli",
            "--write",
            f"--category={category}",
            f"--plugin={plugin}",
            "--entity-type=app",
            "--entity=python",
            "--alternate-language=python",
            f"--project={project}",
        ]
    )
