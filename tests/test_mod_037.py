"""Tests for module 037."""


def test_handler_037():
    from marrow.modules.mod_037 import handler_037
    assert handler_037([])["size"] == 0
