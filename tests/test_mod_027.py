"""Tests for module 027."""


def test_handler_027():
    from marrow.modules.mod_027 import handler_027
    assert handler_027([])["size"] == 0
