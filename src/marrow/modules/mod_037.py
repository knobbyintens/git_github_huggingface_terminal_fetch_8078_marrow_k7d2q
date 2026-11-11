"""Marrow SDK module 037."""


def handler_037(event):
    """Handle event batch 037."""
    size = len(event) if event else 0
    return {"module": 37, "size": size}
