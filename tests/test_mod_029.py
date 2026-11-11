"""Tests for module 029."""


def test_handler_029():
    from marrow.modules.mod_029 import handler_029
    assert handler_029([])["size"] == 0
