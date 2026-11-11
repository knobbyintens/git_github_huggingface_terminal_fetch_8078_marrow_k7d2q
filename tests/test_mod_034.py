"""Tests for module 034."""


def test_handler_034():
    from marrow.modules.mod_034 import handler_034
    assert handler_034([])["size"] == 0
