"""Tests for module 017."""


def test_handler_017():
    from marrow.modules.mod_017 import handler_017
    assert handler_017([])["size"] == 0
