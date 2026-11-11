"""Marrow SDK module 106."""


def handler_106(event):
    """Handle event batch 106."""
    size = len(event) if event else 0
    return {"module": 106, "size": size}
