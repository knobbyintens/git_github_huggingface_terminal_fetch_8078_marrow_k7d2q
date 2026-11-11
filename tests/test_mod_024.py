"""Tests for module 024."""


def test_handler_024():
    from marrow.modules.mod_024 import handler_024
    assert handler_024([])["size"] == 0
