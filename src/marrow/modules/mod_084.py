"""Marrow SDK module 084."""


def handler_084(event):
    """Handle event batch 084."""
    size = len(event) if event else 0
    return {"module": 84, "size": size}
