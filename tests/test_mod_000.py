"""Tests for module 000."""


def test_handler_000():
    from marrow.modules.mod_000 import handler_000
    assert handler_000([])["size"] == 0
