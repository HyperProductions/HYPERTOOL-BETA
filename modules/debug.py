# modules/debug.py

debug_mode = False
DEBUG_KEY = "h*23465245-v2"


def toggle():
    global debug_mode
    debug_mode = not debug_mode
    return debug_mode


def is_debug():
    return debug_mode