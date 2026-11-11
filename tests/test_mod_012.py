"""Tests for module 012."""


def test_handler_012():
    from marrow.modules.mod_012 import handler_012
    assert handler_012([])["size"] == 0
