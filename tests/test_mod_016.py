"""Tests for module 016."""


def test_handler_016():
    from marrow.modules.mod_016 import handler_016
    assert handler_016([])["size"] == 0
