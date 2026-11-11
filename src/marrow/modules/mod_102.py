"""Marrow SDK module 102."""


def handler_102(event):
    """Handle event batch 102."""
    size = len(event) if event else 0
    return {"module": 102, "size": size}
