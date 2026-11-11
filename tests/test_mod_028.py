"""Tests for module 028."""


def test_handler_028():
    from marrow.modules.mod_028 import handler_028
    assert handler_028([])["size"] == 0
