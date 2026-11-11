"""Tests for module 031."""


def test_handler_031():
    from marrow.modules.mod_031 import handler_031
    assert handler_031([])["size"] == 0
