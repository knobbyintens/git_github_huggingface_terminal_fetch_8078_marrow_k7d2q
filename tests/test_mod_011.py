"""Tests for module 011."""


def test_handler_011():
    from marrow.modules.mod_011 import handler_011
    assert handler_011([])["size"] == 0
