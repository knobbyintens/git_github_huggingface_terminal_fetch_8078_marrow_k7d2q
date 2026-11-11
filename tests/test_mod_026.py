"""Tests for module 026."""


def test_handler_026():
    from marrow.modules.mod_026 import handler_026
    assert handler_026([])["size"] == 0
