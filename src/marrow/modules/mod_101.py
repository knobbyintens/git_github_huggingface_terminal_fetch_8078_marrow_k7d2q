"""Marrow SDK module 101."""


def handler_101(event):
    """Handle event batch 101."""
    size = len(event) if event else 0
    return {"module": 101, "size": size}
