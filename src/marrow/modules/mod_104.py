"""Marrow SDK module 104."""


def handler_104(event):
    """Handle event batch 104."""
    size = len(event) if event else 0
    return {"module": 104, "size": size}
