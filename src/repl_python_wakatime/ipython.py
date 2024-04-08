"""ipython
==========
"""

from collections.abc import Callable
from typing import Any

from IPython.terminal.interactiveshell import TerminalInteractiveShell
from IPython.terminal.prompts import ClassicPrompts, Prompts
from pygments.token import _TokenType
from traitlets.config.loader import Config, LazyConfigValue

from .hooks.wakatime import wakatime_hook


def get_new_prompts_class(
    prompts_class: type,
    hook: Callable = wakatime_hook,
    args: tuple = (),
    kwargs: dict[str, Any] | None = None,
) -> type:
    """Get new prompts class.

    :param prompts_class:
    :type prompts_class: type
    :param hook:
    :type hook: Callable
    :param args:
    :type args: tuple
    :param kwargs:
    :type kwargs: dict[str, Any] | None
    :rtype: type
    """
    if kwargs is None:
        kwargs = {}
    if isinstance(prompts_class, LazyConfigValue):
        prompts_class = ClassicPrompts
    shell = TerminalInteractiveShell()

    class Ps(Prompts):
        """Ps."""

        def in_prompt_tokens(self) -> list[tuple[_TokenType, str]]:
            """In prompt tokens.

            :rtype: list[tuple[_TokenType, str]]
            """
            return prompts_class(shell).in_prompt_tokens()

        def continuation_prompt_tokens(
            self, width: int | None = None
        ) -> list[tuple[_TokenType, str]]:
            """Continuation prompt tokens.

            :param width:
            :type width: int | None
            :rtype: list[tuple[_TokenType, str]]
            """
            return prompts_class(shell).continuation_prompt_tokens(width)

        def rewrite_prompt_tokens(self) -> list[tuple[_TokenType, str]]:
            """Rewrite prompt tokens.

            :rtype: list[tuple[_TokenType, str]]
            """
            return prompts_class(shell).rewrite_prompt_tokens()

        def out_prompt_tokens(self) -> list[tuple[_TokenType, str]]:
            """Out prompt tokens.

            :rtype: list[tuple[_TokenType, str]]
            """
            hook(*args, **kwargs)
            return prompts_class(shell).out_prompt_tokens()

    return Ps


def install_hook(
    c: Config,
    hook: Callable = wakatime_hook,
    args: tuple = (),
    kwargs: dict[str, Any] | None = None,
) -> Config:
    """Install hook.

    :param c:
    :type c: Config
    :param hook:
    :type hook: Callable
    :param args:
    :type args: tuple
    :param kwargs:
    :type kwargs: dict[str, Any] | None
    :rtype: Config
    """
    if kwargs is None:
        kwargs = {"plugin": "repl-ipython-wakatime"}
    c.TerminalInteractiveShell.prompts_class = get_new_prompts_class(  # type: ignore
        c.TerminalInteractiveShell.prompts_class,
        hook,
        args,
        kwargs,  # type: ignore
    )
    return c
