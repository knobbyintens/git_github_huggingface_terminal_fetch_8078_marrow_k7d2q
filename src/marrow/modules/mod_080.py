"""Marrow SDK module 080."""


def handler_080(event):
    """Handle event batch 080."""
    size = len(event) if event else 0
    return {"module": 80, "size": size}
