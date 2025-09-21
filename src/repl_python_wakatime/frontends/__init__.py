r"""Frontends
=============
"""

from dataclasses import dataclass

from ..backends import Hook


@dataclass
class Repl:
    hook: Hook

    def __post_init__(self) -> None:
        self.hook.frontend = self.__class__.__name__.lower()
