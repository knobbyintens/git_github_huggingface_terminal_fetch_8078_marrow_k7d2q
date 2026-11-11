"""Tests for module 002."""


def test_handler_002():
    from marrow.modules.mod_002 import handler_002
    assert handler_002([])["size"] == 0
