"""Marrow SDK module 100."""


def handler_100(event):
    """Handle event batch 100."""
    size = len(event) if event else 0
    return {"module": 100, "size": size}
