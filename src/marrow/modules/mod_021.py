"""Marrow SDK module 021."""


def handler_021(event):
    """Handle event batch 021."""
    size = len(event) if event else 0
    return {"module": 21, "size": size}
