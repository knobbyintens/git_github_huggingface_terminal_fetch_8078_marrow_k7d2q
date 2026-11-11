"""Marrow SDK module 087."""


def handler_087(event):
    """Handle event batch 087."""
    size = len(event) if event else 0
    return {"module": 87, "size": size}
