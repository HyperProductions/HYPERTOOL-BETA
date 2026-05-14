import os
import sys
import webbrowser

from modules import systeminfo, ipscanner, portscanner, network, processviewer, cleaner

# COLORS
MOR = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"
GRAY = "\033[90m"
RED = "\033[91m"
GREEN = "\033[92m"

DEBUG_KEY = "h*23465245-V2"
debug_mode = False

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    print(MOR + BOLD)
    print(r"""
---------------------------------------------------------------------------
██   ██ ██    ██ ██████  ███████ ██████  ████████  ██████   ██████  ██
██   ██  ██  ██  ██   ██ ██      ██   ██    ██    ██    ██ ██    ██ ██
███████   ████   ██████  █████   ██████     ██    ██    ██ ██    ██ ██
██   ██    ██    ██      ██      ██   ██    ██    ██    ██ ██    ██ ██
██   ██    ██    ██      ███████ ██   ██    ██     ██████   ██████  ███████
---------------------------------------------------------------------------
    """)
    print(RESET)

def wait():
    input(GRAY + "\nPress Enter to continue..." + RESET)

def iplogger():
    print("IP LOGGER System...")
    webbrowser.open("https://iplogger.org")
    wait()

def debug_panel():
    print(GREEN + "\n[DEBUG MODE]" + RESET)

    files = os.listdir()

    for file in files:
        print(GRAY + file + RESET)

def menu():
    global debug_mode

    while True:
        clear()
        banner()

        if debug_mode:
            print(GREEN + "[ DEBUG MODE ACTIVE ]\n" + RESET)

        print(MOR + "[1]" + RESET + " System Information")
        print(MOR + "[2]" + RESET + " IP Scanner")
        print(MOR + "[3]" + RESET + " Port Scanner")
        print(MOR + "[4]" + RESET + " Network Tools")
        print(MOR + "[5]" + RESET + " Process Viewer")
        print(MOR + "[6]" + RESET + " Cleaner")
        print(MOR + "[7]" + RESET + " IP Logger")

        print(RED + "[0]" + RESET + " Exit")

        choice = input("\n>> Select: ").strip()

        # SECRET DEBUG MODE
        if choice == DEBUG_KEY:h*23465245-v2
            debug_mode = not debug_mode
            print(GREEN + "\nDEBUG MODE TOGGLED!" + RESET)
            wait()
            continue

        if debug_mode and choice == "debug":
            debug_panel()
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
            print(RED + "Shutting down HYPER TOOL..." + RESET)
            break

        else:
            print(RED + "Invalid option!" + RESET)

        wait()

if __name__ == "__main__":
    menu()
