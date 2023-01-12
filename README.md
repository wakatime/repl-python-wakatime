# python-wakatime

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Freed-Wu/python-wakatime/main.svg)](https://results.pre-commit.ci/latest/github/Freed-Wu/python-wakatime/main)
[![github/workflow](https://github.com/Freed-Wu/python-wakatime/actions/workflows/main.yml/badge.svg)](https://github.com/Freed-Wu/python-wakatime/actions)
[![codecov](https://codecov.io/gh/Freed-Wu/python-wakatime/branch/main/graph/badge.svg)](https://codecov.io/gh/Freed-Wu/python-wakatime)
[![readthedocs](https://shields.io/readthedocs/python-wakatime)](https://python-wakatime.readthedocs.io)

[![github/downloads](https://shields.io/github/downloads/Freed-Wu/python-wakatime/total)](https://github.com/Freed-Wu/python-wakatime/releases)
[![github/downloads/latest](https://shields.io/github/downloads/Freed-Wu/python-wakatime/latest/total)](https://github.com/Freed-Wu/python-wakatime/releases/latest)
[![github/issues](https://shields.io/github/issues/Freed-Wu/python-wakatime)](https://github.com/Freed-Wu/python-wakatime/issues)
[![github/issues-closed](https://shields.io/github/issues-closed/Freed-Wu/python-wakatime)](https://github.com/Freed-Wu/python-wakatime/issues?q=is%3Aissue+is%3Aclosed)
[![github/issues-pr](https://shields.io/github/issues-pr/Freed-Wu/python-wakatime)](https://github.com/Freed-Wu/python-wakatime/pulls)
[![github/issues-pr-closed](https://shields.io/github/issues-pr-closed/Freed-Wu/python-wakatime)](https://github.com/Freed-Wu/python-wakatime/pulls?q=is%3Apr+is%3Aclosed)
[![github/discussions](https://shields.io/github/discussions/Freed-Wu/python-wakatime)](https://github.com/Freed-Wu/python-wakatime/discussions)
[![github/milestones](https://shields.io/github/milestones/all/Freed-Wu/python-wakatime)](https://github.com/Freed-Wu/python-wakatime/milestones)
[![github/forks](https://shields.io/github/forks/Freed-Wu/python-wakatime)](https://github.com/Freed-Wu/python-wakatime/network/members)
[![github/stars](https://shields.io/github/stars/Freed-Wu/python-wakatime)](https://github.com/Freed-Wu/python-wakatime/stargazers)
[![github/watchers](https://shields.io/github/watchers/Freed-Wu/python-wakatime)](https://github.com/Freed-Wu/python-wakatime/watchers)
[![github/contributors](https://shields.io/github/contributors/Freed-Wu/python-wakatime)](https://github.com/Freed-Wu/python-wakatime/graphs/contributors)
[![github/commit-activity](https://shields.io/github/commit-activity/w/Freed-Wu/python-wakatime)](https://github.com/Freed-Wu/python-wakatime/graphs/commit-activity)
[![github/last-commit](https://shields.io/github/last-commit/Freed-Wu/python-wakatime)](https://github.com/Freed-Wu/python-wakatime/commits)
[![github/release-date](https://shields.io/github/release-date/Freed-Wu/python-wakatime)](https://github.com/Freed-Wu/python-wakatime/releases/latest)

[![github/license](https://shields.io/github/license/Freed-Wu/python-wakatime)](https://github.com/Freed-Wu/python-wakatime/blob/main/LICENSE)
[![github/languages](https://shields.io/github/languages/count/Freed-Wu/python-wakatime)](https://github.com/Freed-Wu/python-wakatime)
[![github/languages/top](https://shields.io/github/languages/top/Freed-Wu/python-wakatime)](https://github.com/Freed-Wu/python-wakatime)
[![github/directory-file-count](https://shields.io/github/directory-file-count/Freed-Wu/python-wakatime)](https://github.com/Freed-Wu/python-wakatime)
[![github/code-size](https://shields.io/github/languages/code-size/Freed-Wu/python-wakatime)](https://github.com/Freed-Wu/python-wakatime)
[![github/repo-size](https://shields.io/github/repo-size/Freed-Wu/python-wakatime)](https://github.com/Freed-Wu/python-wakatime)
[![github/v](https://shields.io/github/v/release/Freed-Wu/python-wakatime)](https://github.com/Freed-Wu/python-wakatime)

[![pypi/status](https://shields.io/pypi/status/python-wakatime)](https://pypi.org/project/python-wakatime/#description)
[![pypi/v](https://shields.io/pypi/v/python-wakatime)](https://pypi.org/project/python-wakatime/#history)
[![pypi/downloads](https://shields.io/pypi/dd/python-wakatime)](https://pypi.org/project/python-wakatime/#files)
[![pypi/format](https://shields.io/pypi/format/python-wakatime)](https://pypi.org/project/python-wakatime/#files)
[![pypi/implementation](https://shields.io/pypi/implementation/python-wakatime)](https://pypi.org/project/python-wakatime/#files)
[![pypi/pyversions](https://shields.io/pypi/pyversions/python-wakatime)](https://pypi.org/project/python-wakatime/#files)

[wakatime](https://wakatime.com) plugin for python REPLs.

Supported REPLs:

- [x] [python](https://github.com/python/cpython):
  - executes
    [`str(sys.ps1)`](https://docs.python.org/3/library/sys.html#sys.ps1) after
    every input.
  - configure file:
    [`$PYTHON_STARTUP`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONSTARTUP).

```python
from python_wakatime.python import install_hook

install_hook()
```

- [x] [ptpython](https://github.com/prompt-toolkit/ptpython):
  - executes `get_ptpython().get_output_prompt()` after every output.
  - configure file: `.../ptpython/config.py`. `...` depends on OS.

```python
from ptpython.repl import PythonRepl
from python_wakatime.ptpython import install_hook


def configure(repl: PythonRepl) -> None:
    install_hook(repl)
```

- [x] [ipython](https://github.com/ipython/ipython):
  - executes
    `c.TerminalInteractiveShell.prompts_class(shell).out_prompt_tokens()` after
    every output.
  - configure file: `~/.ipython/profile_default/ipython_config.py`.

```python
from python_wakatime.iptpython import install_hook

install_hook(c)
```

- [x] [ptipython](https://github.com/prompt-toolkit/ptpython): Same as
  [ipython](https://github.com/ipython/ipython).
- [ ] [bpython](https://github.com/bpython/bpython)
- [ ] [xonsh](https://github.com/xonsh/xonsh)
- [ ] [mypython](https://github.com/asmeurer/mypython): Won't fix.
  - configure file: non-exist.

`install_hook()` must after customization of prompt string, best at the end of file.

## Similar projects

- <https://wakatime.com/terminal> lists wakatime plugins for many shells.

See more in [document](https://python-wakatime.readthedocs.io).
