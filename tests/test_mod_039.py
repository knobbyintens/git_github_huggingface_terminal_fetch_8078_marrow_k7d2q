"""Tests for module 039."""


def test_handler_039():
    from marrow.modules.mod_039 import handler_039
    assert handler_039([])["size"] == 0
