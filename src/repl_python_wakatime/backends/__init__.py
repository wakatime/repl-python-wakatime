r"""Backends
============
"""

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Self


@dataclass
class Hook:
    r"""Each frontend should pass its name and language. Such as:

    Ptpython(frontend="ptpython", language="python", category="coding")
    Gdb(frontend="gdb", language="gdb", category="debugging")
    """

    frontend: str = "python"
    language: str = "python"
    category: str = "coding"
    hooks: tuple[Self, ...] = ()

    @property
    def plugin(self) -> str:
        """Plugin. ``plugin`` must be the format of ``repl-REPL_NAME-wakatime``
        to let wakatime detect correctly.

        :param self:
        :rtype: str
        """
        if self.category == "coding":
            return f"repl-{self.frontend}-{self.__class__.__name__.lower()}"
        return f"{self.language}-{self.__class__.__name__.lower()}"

    @property
    def language_type(self) -> str:
        return f"Terminal ({self.language})"

    @staticmethod
    def get_project(
        filenames: tuple[str, ...] = (".git/",),
    ) -> str:
        """Get project. Its function is like ``git rev-parse --show-toplevel``.

        use current directory as a fallback.

        :param filenames:
        :type filenames: tuple[str, ...]
        """
        cwd = Path(os.getcwd())
        project = cwd
        for parent in project.parents:
            for filename in filenames:
                path = parent / filename
                if path.exists():
                    return parent.name
        return cwd.name

    def __or__(self, hook: Self) -> "Hook":
        return Hook(hooks=(self, hook))

    def __call__(self) -> None:
        r"""Run hook"""
        for hook in self.hooks:
            hook()
