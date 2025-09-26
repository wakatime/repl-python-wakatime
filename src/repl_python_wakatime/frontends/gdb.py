r"""GDB hook
============

Record your debug time to use gdb in wakatime.
Refer ``https://sourceware.org/gdb/current/onlinedocs/gdb.html/Hooks.html``.
"""

from dataclasses import dataclass

import gdb  # type: ignore
from gdb import Event  # type: ignore

from . import Repl


@dataclass
class StopHook(Repl):
    def __post_init__(self) -> None:
        super().__post_init__()
        self.hook.frontend = "gdb"
        self.hook.language = "gdb"
        self.hook.category = "debugging"
        gdb.events.stop.connect(self.handler)

    def handler(self, _: Event) -> None:
        """Handler.

        :param self:
        :param _:
        :type _: Event
        :rtype: None
        """
        self()
