"""Marrow SDK module 009."""


def handler_009(event):
    """Handle event batch 009."""
    size = len(event) if event else 0
    return {"module": 9, "size": size}
