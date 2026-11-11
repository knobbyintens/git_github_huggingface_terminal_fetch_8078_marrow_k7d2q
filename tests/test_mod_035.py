"""Tests for module 035."""


def test_handler_035():
    from marrow.modules.mod_035 import handler_035
    assert handler_035([])["size"] == 0
