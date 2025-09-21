"""python
=========
"""

import sys
from dataclasses import dataclass

from ..frontends import Repl


@dataclass
class Python(Repl):
    """Python."""

    ps1: object = (sys.ps1 if hasattr(sys, "ps1") else ">>> ",)

    def __post_init__(self) -> None:
        super().__post_init__()

    def __get_attr__(self, name: str):
        return getattr(self.ps1, name)

    def __str__(self) -> str:
        """Str.

        :rtype: str
        """
        self.hook()
        return str(self.ps1)
