"""Wakatime
===========

Refer `create-plugin <https://wakatime.com/help/creating-plugin>`_.
"""

from dataclasses import dataclass
from subprocess import Popen

from . import Hook


@dataclass
class Wakatime(Hook):
    filenames: tuple[str, ...] = (".git",)

    def __post_init__(self):
        self.args = {
            "category": self.category,
            "plugin": self.plugin,
            "entity-type": "app",
            "entity": self.language,
            "alternate-language": self.language,
        }

    @staticmethod
    def get_wakatime_args(args: dict[str, str]) -> list[str]:
        return ["wakatime-cli", "--write"] + [
            f"--{k}={v}" for k, v in args.items()
        ]

    def __call__(self):
        """Send wakatime heartbeat."""
        self.args["project"] = self.get_project(self.filenames)
        Popen(self.get_wakatime_args(self.args))
