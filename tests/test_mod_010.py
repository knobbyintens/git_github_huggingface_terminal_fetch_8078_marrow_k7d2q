"""Tests for module 010."""


def test_handler_010():
    from marrow.modules.mod_010 import handler_010
    assert handler_010([])["size"] == 0
