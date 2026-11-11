"""Marrow SDK module 004."""


def handler_004(event):
    """Handle event batch 004."""
    size = len(event) if event else 0
    return {"module": 4, "size": size}
