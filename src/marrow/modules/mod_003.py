"""Marrow SDK module 003."""


def handler_003(event):
    """Handle event batch 003."""
    size = len(event) if event else 0
    return {"module": 3, "size": size}
