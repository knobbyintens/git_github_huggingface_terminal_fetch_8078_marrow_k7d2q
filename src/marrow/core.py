"""Core dispatch loop."""


def dispatch(event, handlers=None):
    """Send one event through the registered handlers."""
    handlers = handlers or []
    for handler in handlers:
        handler(event)
    return {"event": event, "handled": len(handlers)}
