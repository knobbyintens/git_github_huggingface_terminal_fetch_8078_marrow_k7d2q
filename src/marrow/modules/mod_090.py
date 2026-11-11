"""Marrow SDK module 090."""


def handler_090(event):
    """Handle event batch 090."""
    size = len(event) if event else 0
    return {"module": 90, "size": size}
