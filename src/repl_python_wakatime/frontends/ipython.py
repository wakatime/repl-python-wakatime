"""ipython
==========
"""

from dataclasses import dataclass

from IPython.terminal.prompts import Prompts
from pygments.token import _TokenType

from ..frontends import Repl


@dataclass
class Ipython(Repl, Prompts):
    """Ps."""

    prompts: Prompts

    def __post_init__(self) -> None:
        super().__post_init__()

    def __get_attr__(self, name: str):
        return getattr(self.prompts, name)

    def out_prompt_tokens(self) -> list[tuple[_TokenType, str]]:
        """Out prompt tokens.

        :rtype: list[tuple[_TokenType, str]]
        """
        self()
        return self.prompts.out_prompt_tokens()
