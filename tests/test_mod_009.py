"""Tests for module 009."""


def test_handler_009():
    from marrow.modules.mod_009 import handler_009
    assert handler_009([])["size"] == 0
