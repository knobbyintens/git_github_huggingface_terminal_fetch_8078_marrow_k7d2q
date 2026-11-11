"""Tests for module 030."""


def test_handler_030():
    from marrow.modules.mod_030 import handler_030
    assert handler_030([])["size"] == 0
