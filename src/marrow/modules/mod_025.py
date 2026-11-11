"""Marrow SDK module 025."""


def handler_025(event):
    """Handle event batch 025."""
    size = len(event) if event else 0
    return {"module": 25, "size": size}
