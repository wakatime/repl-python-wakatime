"""ptpython
===========
"""

from dataclasses import dataclass

from prompt_toolkit.formatted_text import AnyFormattedText
from ptpython.prompt_style import PromptStyle

from ..frontends import Repl


@dataclass
class Ptpython(Repl, PromptStyle):
    """Ps."""

    prompt_style: PromptStyle

    def __post_init__(self) -> None:
        super().__post_init__()

    def __get_attr__(self, name: str):
        return getattr(self.prompt_style, name)

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
        self.hook()
        return self.prompt_style.out_prompt()
