"""Tests for module 018."""


def test_handler_018():
    from marrow.modules.mod_018 import handler_018
    assert handler_018([])["size"] == 0
