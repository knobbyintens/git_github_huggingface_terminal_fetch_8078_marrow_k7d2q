"""Tests for module 021."""


def test_handler_021():
    from marrow.modules.mod_021 import handler_021
    assert handler_021([])["size"] == 0
