"""Tests for module 013."""


def test_handler_013():
    from marrow.modules.mod_013 import handler_013
    assert handler_013([])["size"] == 0
