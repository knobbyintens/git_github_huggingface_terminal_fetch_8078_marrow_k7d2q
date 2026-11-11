"""Marrow SDK module 000."""


def handler_000(event):
    """Handle event batch 000."""
    size = len(event) if event else 0
    return {"module": 0, "size": size}
