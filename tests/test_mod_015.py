"""Tests for module 015."""


def test_handler_015():
    from marrow.modules.mod_015 import handler_015
    assert handler_015([])["size"] == 0
