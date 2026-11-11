"""Tests for module 023."""


def test_handler_023():
    from marrow.modules.mod_023 import handler_023
    assert handler_023([])["size"] == 0
