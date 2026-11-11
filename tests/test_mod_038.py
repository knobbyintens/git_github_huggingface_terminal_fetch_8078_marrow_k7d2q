"""Tests for module 038."""


def test_handler_038():
    from marrow.modules.mod_038 import handler_038
    assert handler_038([])["size"] == 0
