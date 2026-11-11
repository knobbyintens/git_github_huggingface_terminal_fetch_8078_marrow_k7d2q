"""Tests for module 032."""


def test_handler_032():
    from marrow.modules.mod_032 import handler_032
    assert handler_032([])["size"] == 0
