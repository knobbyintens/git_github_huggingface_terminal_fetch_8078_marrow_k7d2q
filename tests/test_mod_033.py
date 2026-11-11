"""Tests for module 033."""


def test_handler_033():
    from marrow.modules.mod_033 import handler_033
    assert handler_033([])["size"] == 0
