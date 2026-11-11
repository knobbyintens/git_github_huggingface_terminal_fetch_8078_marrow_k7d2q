"""Marrow SDK module 001."""


def handler_001(event):
    """Handle event batch 001."""
    size = len(event) if event else 0
    return {"module": 1, "size": size}
