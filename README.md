# repl-python-wakatime

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/wakatime/repl-python-wakatime/main.svg)](https://results.pre-commit.ci/latest/github/wakatime/repl-python-wakatime/main)
[![github/workflow](https://github.com/wakatime/repl-python-wakatime/actions/workflows/main.yml/badge.svg)](https://github.com/wakatime/repl-python-wakatime/actions)
[![codecov](https://codecov.io/gh/wakatime/repl-python-wakatime/branch/main/graph/badge.svg)](https://codecov.io/gh/wakatime/repl-python-wakatime)
[![readthedocs](https://shields.io/readthedocs/repl-python-wakatime)](https://repl-python-wakatime.readthedocs.io)

[![github/downloads](https://shields.io/github/downloads/wakatime/repl-python-wakatime/total)](https://github.com/wakatime/repl-python-wakatime/releases)
[![github/downloads/latest](https://shields.io/github/downloads/wakatime/repl-python-wakatime/latest/total)](https://github.com/wakatime/repl-python-wakatime/releases/latest)
[![github/issues](https://shields.io/github/issues/wakatime/repl-python-wakatime)](https://github.com/wakatime/repl-python-wakatime/issues)
[![github/issues-closed](https://shields.io/github/issues-closed/wakatime/repl-python-wakatime)](https://github.com/wakatime/repl-python-wakatime/issues?q=is%3Aissue+is%3Aclosed)
[![github/issues-pr](https://shields.io/github/issues-pr/wakatime/repl-python-wakatime)](https://github.com/wakatime/repl-python-wakatime/pulls)
[![github/issues-pr-closed](https://shields.io/github/issues-pr-closed/wakatime/repl-python-wakatime)](https://github.com/wakatime/repl-python-wakatime/pulls?q=is%3Apr+is%3Aclosed)
[![github/discussions](https://shields.io/github/discussions/wakatime/repl-python-wakatime)](https://github.com/wakatime/repl-python-wakatime/discussions)
[![github/milestones](https://shields.io/github/milestones/all/wakatime/repl-python-wakatime)](https://github.com/wakatime/repl-python-wakatime/milestones)
[![github/forks](https://shields.io/github/forks/wakatime/repl-python-wakatime)](https://github.com/wakatime/repl-python-wakatime/network/members)
[![github/stars](https://shields.io/github/stars/wakatime/repl-python-wakatime)](https://github.com/wakatime/repl-python-wakatime/stargazers)
[![github/watchers](https://shields.io/github/watchers/wakatime/repl-python-wakatime)](https://github.com/wakatime/repl-python-wakatime/watchers)
[![github/contributors](https://shields.io/github/contributors/wakatime/repl-python-wakatime)](https://github.com/wakatime/repl-python-wakatime/graphs/contributors)
[![github/commit-activity](https://shields.io/github/commit-activity/w/wakatime/repl-python-wakatime)](https://github.com/wakatime/repl-python-wakatime/graphs/commit-activity)
[![github/last-commit](https://shields.io/github/last-commit/wakatime/repl-python-wakatime)](https://github.com/wakatime/repl-python-wakatime/commits)
[![github/release-date](https://shields.io/github/release-date/wakatime/repl-python-wakatime)](https://github.com/wakatime/repl-python-wakatime/releases/latest)

[![github/license](https://shields.io/github/license/wakatime/repl-python-wakatime)](https://github.com/wakatime/repl-python-wakatime/blob/main/LICENSE)
[![github/languages](https://shields.io/github/languages/count/wakatime/repl-python-wakatime)](https://github.com/wakatime/repl-python-wakatime)
[![github/languages/top](https://shields.io/github/languages/top/wakatime/repl-python-wakatime)](https://github.com/wakatime/repl-python-wakatime)
[![github/directory-file-count](https://shields.io/github/directory-file-count/wakatime/repl-python-wakatime)](https://github.com/wakatime/repl-python-wakatime)
[![github/code-size](https://shields.io/github/languages/code-size/wakatime/repl-python-wakatime)](https://github.com/wakatime/repl-python-wakatime)
[![github/repo-size](https://shields.io/github/repo-size/wakatime/repl-python-wakatime)](https://github.com/wakatime/repl-python-wakatime)
[![github/v](https://shields.io/github/v/release/wakatime/repl-python-wakatime)](https://github.com/wakatime/repl-python-wakatime)

[![pypi/status](https://shields.io/pypi/status/repl-python-wakatime)](https://pypi.org/project/repl-python-wakatime/#description)
[![pypi/v](https://shields.io/pypi/v/repl-python-wakatime)](https://pypi.org/project/repl-python-wakatime/#history)
[![pypi/downloads](https://shields.io/pypi/dd/repl-python-wakatime)](https://pypi.org/project/repl-python-wakatime/#files)
[![pypi/format](https://shields.io/pypi/format/repl-python-wakatime)](https://pypi.org/project/repl-python-wakatime/#files)
[![pypi/implementation](https://shields.io/pypi/implementation/repl-python-wakatime)](https://pypi.org/project/repl-python-wakatime/#files)
[![pypi/pyversions](https://shields.io/pypi/pyversions/repl-python-wakatime)](https://pypi.org/project/repl-python-wakatime/#files)

Python REPL plugin for automatic time tracking and metrics generated from your
programming activity.

![screen](https://github.com/user-attachments/assets/4e337cae-06a7-4164-be83-c7b73e8a0f63)

## REPLs

### [python](https://github.com/python/cpython)

[`$PYTHON_STARTUP`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONSTARTUP):

```python
import sys

from repl_python_wakatime.backends.wakatime import Wakatime
from repl_python_wakatime.frontends.python import Python

sys.ps1 = Python(Wakatime())
```

### [ptpython](https://github.com/prompt-toolkit/ptpython)

`${XDG_CONFIG_HOME:-$HOME/.config}/ptpython/config.py`:

```python
from repl_python_wakatime.backends.wakatime import Wakatime
from repl_python_wakatime.frontends.ptpython import Ptpython


def configure(repl: PythonRepl) -> None:
    repl.all_prompt_styles[repl.prompt_style] = Ptpython(
        Wakatime(), repl.all_prompt_styles[repl.prompt_style]
    )
```

### [ipython](https://github.com/ipython/ipython)/[ptipython](https://github.com/prompt-toolkit/ptpython)

`~/.ipython/profile_default/ipython_config.py`:

```python
from repl_python_wakatime.backends.wakatime import Wakatime
from repl_python_wakatime.frontends.ipython import Ipython

c.TerminalInteractiveShell.prompts_class = lambda *args, **kwargs: Ipython(
    Wakatime(),
    c.TerminalInteractiveShell.prompts_class(*args, **kwargs),
)
```

### [gdb](https://sourceware.org/gdb/)

Your `gdb` must be compiled with
[python port](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Python.html).

`~/.config/gdb/gdbinit`:

```gdb
source ~/.config/gdb/gdbinit.py
```

`~/.config/gdb/gdbinit.py`:

```python
from repl_python_wakatime.backends.wakatime import Wakatime
from repl_python_wakatime.frontends.gdb import StopHook

StopHook(Wakatime())
```

- [ ] [bpython](https://github.com/bpython/bpython)
- [ ] [xonsh](https://github.com/xonsh/xonsh)
- [ ] [mypython](https://github.com/asmeurer/mypython): won't fix due to no any
  configuration.
- [ ] vim/neovim with python support: see
  [vim-wakatime](https://github.com/wakatime/vim-wakatime) and
  [code-stats.nvim](https://github.com/Freed-Wu/code-stats.nvim)

## Hooks

- [x] [wakatime](https://wakatime.com/)
- [x] [codestats](https://codestats.net/)
- [ ] [codetime](https://codetime.dev/)
- [ ] [rescuetime](https://www.rescuetime.com/)

You can use many hooks at the same time:

```python
from repl_python_wakatime.backends.chainedhook import ChainedHook
from repl_python_wakatime.backends.codestats import CodeStats
from repl_python_wakatime.backends.wakatime import Wakatime
from repl_python_wakatime.frontends.python import Python

sys.ps1 = Python(ChainedHook(hooks=(Wakatime(), CodeStats())))
```

## APIs

You can use this project to statistic the time of using any programs. Such as,
[translate-shell](https://github.com/Freed-Wu/translate-shell/) is a translating
program:

```python
from repl_python_wakatime.backends.wakatime import Wakatime
from repl_python_wakatime.frontends import Repl

repl = Repl(Wakatime(language="translate-shell", category="translating"))
# after each translating
repl()
```

## Similar projects

- [wakatime plugins for python and many shells](https://wakatime.com/terminal)
- [codestats plugins](https://codestats.net/plugins)
