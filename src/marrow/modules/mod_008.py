"""Marrow SDK module 008."""


def handler_008(event):
    """Handle event batch 008."""
    size = len(event) if event else 0
    return {"module": 8, "size": size}
