"""Marrow SDK module 070."""


def handler_070(event):
    """Handle event batch 070."""
    size = len(event) if event else 0
    return {"module": 70, "size": size}
