"""Tests for module 005."""


def test_handler_005():
    from marrow.modules.mod_005 import handler_005
    assert handler_005([])["size"] == 0
