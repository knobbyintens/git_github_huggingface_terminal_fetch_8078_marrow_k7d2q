"""Tests for module 007."""


def test_handler_007():
    from marrow.modules.mod_007 import handler_007
    assert handler_007([])["size"] == 0
