"""Marrow SDK module 091."""


def handler_091(event):
    """Handle event batch 091."""
    size = len(event) if event else 0
    return {"module": 91, "size": size}
