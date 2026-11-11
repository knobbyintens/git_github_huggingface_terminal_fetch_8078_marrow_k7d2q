"""Marrow SDK module 093."""


def handler_093(event):
    """Handle event batch 093."""
    size = len(event) if event else 0
    return {"module": 93, "size": size}
