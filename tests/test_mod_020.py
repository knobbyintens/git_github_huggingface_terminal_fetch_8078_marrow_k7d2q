"""Tests for module 020."""


def test_handler_020():
    from marrow.modules.mod_020 import handler_020
    assert handler_020([])["size"] == 0
