"""Marrow SDK module 027."""


def handler_027(event):
    """Handle event batch 027."""
    size = len(event) if event else 0
    return {"module": 27, "size": size}
