"""Tests for module 036."""


def test_handler_036():
    from marrow.modules.mod_036 import handler_036
    assert handler_036([])["size"] == 0
