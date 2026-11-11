"""Tests for module 004."""


def test_handler_004():
    from marrow.modules.mod_004 import handler_004
    assert handler_004([])["size"] == 0
