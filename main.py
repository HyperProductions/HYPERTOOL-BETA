import os
import sys
import webbrowser

from modules import systeminfo, ipscanner, portscanner, network, processviewer, cleaner
from modules import debug

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


def iplogger():
    webbrowser.open("https://iplogger.org")
    wait()


def menu():
    while True:
        clear()

        # NORMAL MODE
        if not debug.is_debug():
            banner()

            print("[1] System Info")
            print("[2] IP Scanner")
            print("[3] Port Scanner")
            print("[4] Network Tools")
            print("[5] Process Viewer")
            print("[6] Cleaner")
            print("[7] IP Logger")
            print("[0] Exit")

            choice = input("\n>> ").strip().lower()

        # RETRO DEBUG MODE
        else:
            debug.retro_banner()
            debug.retro_menu()

            choice = input("\nDEBUG>> ").strip().lower()

            if choice == "5":
                debug.toggle()
                continue

            print("\n[DEBUG OUTPUT]")
            print("Command:", choice)
            wait()
            continue

        # SECRET KEY
        if choice == debug.DEBUG_KEY:
            debug.toggle()
            print(GREEN + "\nDEBUG MODE TOGGLED" + RESET)
            wait()
            continue

        clear()

        if choice == "1":
            systeminfo.run()

        elif choice == "2":
            ipscanner.run()

        elif choice == "3":
            portscanner.run()

        elif choice == "4":
            network.run()

        elif choice == "5":
            processviewer.run()

        elif choice == "6":
            cleaner.run()

        elif choice == "7":
            iplogger()

        elif choice == "0":
            sys.exit()

        else:
            print(RED + "Invalid option!" + RESET)

        wait()


if __name__ == "__main__":
    menu()