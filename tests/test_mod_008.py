"""Tests for module 008."""


def test_handler_008():
    from marrow.modules.mod_008 import handler_008
    assert handler_008([])["size"] == 0
