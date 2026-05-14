import os
import sys
import webbrowser

from modules import systeminfo, ipscanner, portscanner, network, processviewer, cleaner
from modules import debug

# COLORS
MOR = "\033[95m"
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
GRAY = "\033[90m"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    print(MOR + r"""
---------------------------------------------------------------------------
██   ██ ██    ██ ██████  ███████ ██████  ████████  ██████   ██████  ██
██   ██  ██  ██  ██   ██ ██      ██   ██    ██    ██    ██ ██    ██ ██
███████   ████   ██████  █████   ██████     ██    ██    ██ ██    ██ ██
██   ██    ██    ██      ██      ██   ██    ██    ██    ██ ██    ██ ██
██   ██    ██    ██      ███████ ██   ██    ██     ██████   ██████  ███████
---------------------------------------------------------------------------
""" + RESET)


def wait():
    input(GRAY + "\nPress Enter..." + RESET)


# 🔥 SAFE RUN (CRASH PROTECTION)
def safe_run(module):
    try:
        module.run()
    except Exception as e:
        print(RED + "\nMODULE ERROR:" + RESET, e)
        wait()


def iplogger():
    print(MOR + "Opening IP Logger..." + RESET)
    webbrowser.open("https://iplogger.org")
    wait()


def menu():
    while True:
        clear()

        # NORMAL MODE
        if not debug.is_debug():
            banner()

            print(MOR + "[1]" + RESET + " System Information")
            print(MOR + "[2]" + RESET + " IP Scanner")
            print(MOR + "[3]" + RESET + " Port Scanner")
            print(MOR + "[4]" + RESET + " Network Tools")
            print(MOR + "[5]" + RESET + " Process Viewer")
            print(MOR + "[6]" + RESET + " Cleaner")
            print(MOR + "[7]" + RESET + " IP Logger")
            print(RED + "[0]" + RESET + " Exit")

            choice = input("\n>> Select: ").strip().lower()

        # DEBUG MODE
        else:
            debug.retro_banner()
            debug.retro_menu()

            choice = input(MOR + "\nDEBUG>> " + RESET).strip().lower()

            if choice == "5":
                debug.toggle()
                continue

            print(MOR + "\n[DEBUG OUTPUT]" + RESET)
            print(MOR + "Command:", choice + RESET)
            wait()
            continue

        # SECRET DEBUG KEY
        if choice == debug.DEBUG_KEY:
            state = debug.toggle()
            print(GREEN + f"\nDEBUG MODE: {state}" + RESET)
            wait()
            continue

        clear()

        if choice == "1":
            safe_run(systeminfo)

        elif choice == "2":
            safe_run(ipscanner)

        elif choice == "3":
            safe_run(portscanner)

        elif choice == "4":
            safe_run(network)

        elif choice == "5":
            safe_run(processviewer)

        elif choice == "6":
            safe_run(cleaner)

        elif choice == "7":
            iplogger()

        elif choice == "0":
            sys.exit()

        else:
            print(RED + "Invalid option!" + RESET)
            wait()


if __name__ == "__main__":
    menu()
