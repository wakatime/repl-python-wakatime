"""python
=========
"""
import sys
from typing import Any, Callable

from .hooks.wakatime import wakatime_hook


class Ps1:
    """Ps1."""

    def __init__(
        self,
        ps1: object = None,
        hook: Callable = wakatime_hook,
        args: tuple = (),
        kwargs: dict[str, Any] = {},
    ) -> None:
        """Init.

        :param ps1:
        :type ps1: object
        :param hook:
        :type hook: Callable
        :param args:
        :type args: tuple
        :param kwargs:
        :type kwargs: dict[str, Any]
        :rtype: None
        """
        if ps1:
            self.ps1 = ps1
        else:
            if hasattr(sys, "ps1"):
                self.ps1 = sys.ps1
            else:
                self.ps1 = ">>> "
        self.hook = hook
        self.args = args
        self.kwargs = kwargs

    def __str__(self) -> str:
        """Str.

        :rtype: str
        """
        self.hook(*self.args, **self.kwargs)
        if isinstance(self.ps1, str):
            return self.ps1
        else:
            return str(self.ps1)


def install_hook(
    hook: Callable = wakatime_hook,
    args: tuple = (),
    kwargs: dict[str, Any] = {"plugin": "repl-python-wakatime"},
) -> object:
    """Install hook.

    :param hook:
    :type hook: Callable
    :param args:
    :type args: tuple
    :param kwargs:
    :type kwargs: dict[str, Any]
    :rtype: object
    """
    sys.ps1 = Ps1(hook=hook, args=args, kwargs=kwargs)
    return sys.ps1
