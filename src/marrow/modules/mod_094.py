"""Marrow SDK module 094."""


def handler_094(event):
    """Handle event batch 094."""
    size = len(event) if event else 0
    return {"module": 94, "size": size}
