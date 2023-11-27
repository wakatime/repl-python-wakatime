"""Test Project
===============
"""
import os
from pathlib import Path

from repl_python_wakatime.utils.project import get_project


class Test:
    """Test."""

    def test_get_project_no_cwd(self, tmp_path: Path) -> None:
        """Test get project no cwd.

        :param tmp_path:
        :type tmp_path: Path
        :rtype: None
        """
        os.chdir(tmp_path)
        os.makedirs(".svn")
        os.makedirs("subdir")
        os.chdir("subdir")
        rst = get_project([".git", ".svn"])
        expected = os.path.basename(tmp_path)
        assert rst == expected

    def test_get_project_cwd(self, tmp_path: Path) -> None:
        """Test get project cwd.

        :param tmp_path:
        :type tmp_path: Path
        :rtype: None
        """
        os.chdir(tmp_path)
        os.makedirs("subdir")
        os.chdir("subdir")
        rst = get_project([".git", ".svn"])
        expected = "subdir"
        assert rst == expected
