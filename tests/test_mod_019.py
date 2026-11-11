"""Tests for module 019."""


def test_handler_019():
    from marrow.modules.mod_019 import handler_019
    assert handler_019([])["size"] == 0
