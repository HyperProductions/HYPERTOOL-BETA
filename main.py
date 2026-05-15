import os
import sys
import platform
import webbrowser

from modules import ipscanner, portscanner, network, cleaner, debug

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


# ✅ OPTION 1 FIX
def system_info():
    print(MOR + "\n=== SYSTEM INFO ===\n" + RESET)

    print("OS:", platform.system())
    print("Version:", platform.version())
    print("Machine:", platform.machine())
    print("Processor:", platform.processor())

    wait()


# ✅ OPTION 5 FIX
def process_viewer():
    print(MOR + "\n=== PROCESS VIEWER ===\n" + RESET)

    os.system("ps")

    wait()


# OPTION 7
def iplogger():
    print(MOR + "Opening IP Logger..." + RESET)
    webbrowser.open("https://iplogger.org")
    wait()


# SAFE MODULE RUN
def safe_run(module):
    try:
        module.run()
    except Exception as e:
        print(RED + "\nMODULE ERROR:" + RESET, e)
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
            debug.toggle()

            print(GREEN + "\nDEBUG MODE TOGGLED" + RESET)

            wait()
            continue

        clear()

        # ✅ 1 FIXED
        if choice == "1":
            system_info()

        # NORMAL MODULES
        elif choice == "2":
            safe_run(ipscanner)

        elif choice == "3":
            safe_run(portscanner)

        elif choice == "4":
            safe_run(network)

        # ✅ 5 FIXED
        elif choice == "5":
            process_viewer()

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
