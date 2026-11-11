"""Marrow SDK module 017."""


def handler_017(event):
    """Handle event batch 017."""
    size = len(event) if event else 0
    return {"module": 17, "size": size}
