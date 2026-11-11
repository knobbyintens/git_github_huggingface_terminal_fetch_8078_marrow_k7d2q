"""Tests for module 022."""


def test_handler_022():
    from marrow.modules.mod_022 import handler_022
    assert handler_022([])["size"] == 0
