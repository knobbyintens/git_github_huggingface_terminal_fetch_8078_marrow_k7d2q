"""Marrow SDK module 036."""


def handler_036(event):
    """Handle event batch 036."""
    size = len(event) if event else 0
    return {"module": 36, "size": size}
