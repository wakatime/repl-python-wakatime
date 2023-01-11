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

[wakatime](https://wakatime.com) plugin for python.

## Usage

Add the following code to your
[`$PYTHON_STARTUP`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONSTARTUP):

```python
from python_wakatime import install_hook

# ... # customize your PS1

# must after customization of PS1, best at the end of file
install_hook()
```

## FAQ

Q: How does it work?

A: Python executes
[`str(sys.ps1)`](https://docs.python.org/3/library/sys.html#sys.ps1) after
every inputting of the user. We can do anything what we want in
`sys.ps1.__str__()`.

## Similar projects

- <https://wakatime.com/terminal> lists wakatime plugins for bash/zsh/fish.

See more in [document](https://python-wakatime.readthedocs.io).
