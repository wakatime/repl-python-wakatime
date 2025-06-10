r"""GDB hook
============

Record your debug time to use gdb in wakatime.
"""

import os

import gdb  # type: ignore

hook_names = os.getenv("HOOK_NAMES", "wakatime")

for hook_name in hook_names.split(":"):
    if hook_name == "wakatime":
        from repl_python_wakatime.hooks.wakatime import wakatime_hook as hook
    elif hook_name == "codestats":
        from repl_python_wakatime.hooks.codestats import codestats_hook as hook
    else:
        raise NotImplementedError


class StopHook:
    def __init__(self):
        gdb.events.stop.connect(self.handler)

    def handler(self, event):
        hook(plugin="repl-gdb-wakatime", language="gdb", category="debugging")


StopHook()
