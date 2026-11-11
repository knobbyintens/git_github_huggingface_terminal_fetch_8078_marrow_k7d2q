"""Marrow SDK module 013."""


def handler_013(event):
    """Handle event batch 013."""
    size = len(event) if event else 0
    return {"module": 13, "size": size}
