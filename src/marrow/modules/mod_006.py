"""Marrow SDK module 006."""


def handler_006(event):
    """Handle event batch 006."""
    size = len(event) if event else 0
    return {"module": 6, "size": size}
