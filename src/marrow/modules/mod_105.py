"""Marrow SDK module 105."""


def handler_105(event):
    """Handle event batch 105."""
    size = len(event) if event else 0
    return {"module": 105, "size": size}
