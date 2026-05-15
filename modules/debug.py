debug_mode = False
DEBUG_KEY = "h*23465245-v2"

MOR = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"


def toggle():
    global debug_mode
    debug_mode = not debug_mode
    return debug_mode


def is_debug():
    return debug_mode


def retro_banner():
    print(MOR + BOLD)
    print(r"""
========================================
   H Y P E R T O O L   D E B U G
        CLASSIFIED SYSTEM
         EST. 1980 TERMINAL
========================================
""")
    print(RESET)


def retro_menu():
    print(MOR)
    print("""
[1] SYSTEM INFO DUMP
[2] PROCESS TABLE
[3] NETWORK TRACE
[4] FILE LIST
[5] EXIT DEBUG MODE
""")
    print(RESET)