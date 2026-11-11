"""Tests for module 006."""


def test_handler_006():
    from marrow.modules.mod_006 import handler_006
    assert handler_006([])["size"] == 0
