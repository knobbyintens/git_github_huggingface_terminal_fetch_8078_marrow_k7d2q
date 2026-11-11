"""Marrow SDK module 062."""


def handler_062(event):
    """Handle event batch 062."""
    size = len(event) if event else 0
    return {"module": 62, "size": size}
