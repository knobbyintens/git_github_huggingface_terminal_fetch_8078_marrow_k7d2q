"""Tests for module 001."""


def test_handler_001():
    from marrow.modules.mod_001 import handler_001
    assert handler_001([])["size"] == 0
