"""Project
==========
"""

import os
from typing import Callable


def get_project(
    filenames: list[str] = [".git"],
    detect_func: Callable[[str], bool] = os.path.isdir,
) -> str:
    """Get project. Its function is like ``git rev-parse --show-toplevel``.

    If ``.git`` is a directory, use current directory. If not, detect its
    parent directory. If its parent directory is itself (which means it is the
    root directory) and ``.git`` is still not a directory, stop detection. Just
    use current directory as ``project``.

    :param filenames:
    :type filenames: list[str]
    :param detect_func:
    :type detect_func: Callable[[str], bool]
    """
    cwd = os.getcwd()
    project = cwd
    oldproject = ""
    while not any(
        detect_func(os.path.join(project, filename)) for filename in filenames
    ):
        if oldproject == project:
            project = cwd
            break
        oldproject = project
        project = os.path.dirname(project)
    project = os.path.basename(project)
    return project
