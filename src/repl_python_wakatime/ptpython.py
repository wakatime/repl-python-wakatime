"""ptpython
===========
"""

from typing import Any, Callable

from prompt_toolkit.formatted_text import AnyFormattedText
from ptpython.prompt_style import PromptStyle
from ptpython.repl import PythonRepl

from .hooks.wakatime import wakatime_hook


class Ps(PromptStyle):
    """Ps."""

    def __init__(
        self,
        prompt_style: PromptStyle,
        hook: Callable = wakatime_hook,
        args: tuple = (),
        kwargs: dict[str, Any] = {},
    ) -> None:
        """Init.

        :param prompt_style:
        :type prompt_style: PromptStyle
        :param hook:
        :type hook: Callable
        :param args:
        :type args: tuple
        :param kwargs:
        :type kwargs: dict[str, Any]
        :rtype: None
        """
        super().__init__()
        self.prompt_style = prompt_style
        self.hook = hook
        self.args = args
        self.kwargs = kwargs

    def in_prompt(self) -> AnyFormattedText:
        """Return the input tokens.

        :rtype: AnyFormattedText
        """
        return self.prompt_style.in_prompt()

    def in2_prompt(self, width: int) -> AnyFormattedText:
        """Tokens for every following input line.

        :param width: The available width. This is coming from the width taken
                      by `in_prompt`.
        :type width: int
        :rtype: AnyFormattedText
        """
        return self.prompt_style.in2_prompt(width)

    def out_prompt(self) -> AnyFormattedText:
        """Return the output tokens.

        :rtype: AnyFormattedText
        """
        self.hook(*self.args, **self.kwargs)
        return self.prompt_style.out_prompt()


def install_hook(
    repl: PythonRepl,
    hook: Callable = wakatime_hook,
    args: tuple = (),
    kwargs: dict[str, Any] = {"plugin": "repl-ptpython-wakatime"},
    hook_prefix: str = "ps1_",
) -> PythonRepl:
    """Install hook.

    :param repl:
    :type repl: PythonRepl
    :param hook:
    :type hook: Callable
    :param args:
    :type args: tuple
    :param kwargs:
    :type kwargs: dict[str, Any]
    :param hook_prefix:
    :type hook_prefix: str
    :rtype: PythonRepl
    """
    ps = Ps(repl.all_prompt_styles[repl.prompt_style], hook, args, kwargs)
    length = len(hook_prefix)
    names = map(
        lambda x: x[length:],
        filter(lambda x: x.startswith(hook_prefix), repl.all_prompt_styles),
    )
    number = 0
    while str(number) in names:
        number += 1
    name = hook_prefix + str(number)
    repl.all_prompt_styles |= {name: ps}
    repl.prompt_style = name
    return repl
