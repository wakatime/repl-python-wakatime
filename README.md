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

![screenshot](https://github.com/wakatime/repl-python-wakatime/assets/32936898/d0ac2fab-f9c2-4213-99e3-4249279b1213)

Supported REPLs:

- [x] [python](https://github.com/python/cpython):
  - executes
    [`str(sys.ps1)`](https://docs.python.org/3/library/sys.html#sys.ps1) after
    every input.
  - configure file:
    [`$PYTHON_STARTUP`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONSTARTUP).

```python
from repl_python_wakatime.python import install_hook

install_hook()
```

- [x] [ptpython](https://github.com/prompt-toolkit/ptpython):
  - executes `get_ptpython().get_output_prompt()` after every output.
  - configure file: `.../ptpython/config.py`. `...` depends on OS.

```python
from ptpython.repl import PythonRepl
from repl_python_wakatime.ptpython import install_hook


def configure(repl: PythonRepl) -> None:
    install_hook(repl)
```

- [x] [ipython](https://github.com/ipython/ipython):
  - executes
    `c.TerminalInteractiveShell.prompts_class(shell).out_prompt_tokens()` after
    every output.
  - configure file: `~/.ipython/profile_default/ipython_config.py`.

```python
from repl_python_wakatime.iptpython import install_hook

install_hook(c)
```

- [x] [ptipython](https://github.com/prompt-toolkit/ptpython): Same as
  [ipython](https://github.com/ipython/ipython).
- [ ] [bpython](https://github.com/bpython/bpython)
- [ ] [xonsh](https://github.com/xonsh/xonsh)
- [ ] [mypython](https://github.com/asmeurer/mypython): Won't fix.
  - configure file: non-exist.

`install_hook()` must be after the customization of the prompt string and best
at the end of file.

## Configure

```python
from repl_python_wakatime.python import install_hook

install_hook(hook_function, args, kwargs)
```

will execute `hook_function(*args, **kwargs)` after every output/input. Other
REPLs are similar. Currently, `hook_function` can be:

- `repl_python_wakatime.hooks.wakatime.wakatime_hook()`: By default.
- `repl_python_wakatime.hooks.codestats.codestats_hook()`: for [codestats](https://codestats.net/)
- Create your hooks for other similar projects, such as:
  - [codetime](https://codetime.dev/)
  - [rescuetime](https://www.rescuetime.com/)
  - ...

## Related programs

Some programs is written in python or providing a python port.
We can use this project to statistic their time:

- [gdb](https://sourceware.org/gdb): See
  [here](https://github.com/Freed-Wu/gdb-prompt)

## Similar projects

- [wakatime plugins for python and many shells](https://wakatime.com/terminal)
- [codestats plugins](https://codestats.net/plugins)
