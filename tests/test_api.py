r"""Test API
============
"""

import pytest
from repl_python_wakatime.hooks.codestats import CodeStats
from repl_python_wakatime.utils.api import get_api_key

API_KEY = get_api_key()


class Test:
    r"""Test."""

    @pytest.mark.skipif(API_KEY == "", reason="no API key")
    def test_codestats(self, caplog) -> None:
        """Test codestats.

        :param caplog:
        :rtype: None
        """
        codestats = CodeStats(API_KEY)
        codestats.add_xp()
        assert codestats.xp_dict[codestats.language_type] == 1
        codestats.send_xp()
        assert codestats.xp_dict[codestats.language_type] == 0
        assert caplog.records == []
