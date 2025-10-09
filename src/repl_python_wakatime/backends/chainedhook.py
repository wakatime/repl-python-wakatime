"""Chained Hook
===============

"""

from dataclasses import dataclass
from typing import Any

from . import Hook


@dataclass
class ChainedHook(Hook):
    hooks: tuple[Hook, ...] = ()

    def __call__(self) -> None:
        r"""Run hook"""
        for hook in self.hooks:
            hook()

    def __setattr__(self, k: Any, v: Any) -> None:
        if k in {"frontend", "language", "category"}:
            for hook in self.hooks:
                setattr(hook, k, v)
        super().__setattr__(k, v)
