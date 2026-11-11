"""Marrow SDK module 002."""


def handler_002(event):
    """Handle event batch 002."""
    size = len(event) if event else 0
    return {"module": 2, "size": size}
