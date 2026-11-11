"""Marrow SDK module 096."""


def handler_096(event):
    """Handle event batch 096."""
    size = len(event) if event else 0
    return {"module": 96, "size": size}
