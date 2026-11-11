"""Marrow SDK module 020."""


def handler_020(event):
    """Handle event batch 020."""
    size = len(event) if event else 0
    return {"module": 20, "size": size}
