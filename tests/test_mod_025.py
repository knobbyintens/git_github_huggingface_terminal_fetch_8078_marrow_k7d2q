"""Tests for module 025."""


def test_handler_025():
    from marrow.modules.mod_025 import handler_025
    assert handler_025([])["size"] == 0
