"""Marrow SDK module 103."""


def handler_103(event):
    """Handle event batch 103."""
    size = len(event) if event else 0
    return {"module": 103, "size": size}
