"""Tests for module 014."""


def test_handler_014():
    from marrow.modules.mod_014 import handler_014
    assert handler_014([])["size"] == 0
