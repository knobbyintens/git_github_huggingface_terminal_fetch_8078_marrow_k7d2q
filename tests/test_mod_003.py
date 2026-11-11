"""Tests for module 003."""


def test_handler_003():
    from marrow.modules.mod_003 import handler_003
    assert handler_003([])["size"] == 0
