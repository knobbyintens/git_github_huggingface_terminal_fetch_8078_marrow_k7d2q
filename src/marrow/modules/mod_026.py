"""Marrow SDK module 026."""


def handler_026(event):
    """Handle event batch 026."""
    size = len(event) if event else 0
    return {"module": 26, "size": size}
