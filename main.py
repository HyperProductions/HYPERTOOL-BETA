import os
import sys
import webbrowser

from modules import systeminfo, ipscanner, portscanner, network, processviewer, cleaner

# Colors
MOR = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"
GRAY = "\033[90m"
RED = "\033[91m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    print(MOR + BOLD)
    print(r"""
=================================
       H Y P E R   T O O L
         B E T A  v2.0
=================================
    """)
    print(RESET)

def wait():
    input(GRAY + "\nPress Enter to continue..." + RESET)

def ıp_logger():
    clear()
    print("IP LOGGER System....")
    print("Opening IP LOGGER...")
    webbrowser.open("https://iplogger.org")
    wait()

def menu():
    while True:
        clear()
        banner()

        print(MOR + "[1]" + RESET + " System Information")
        print(MOR + "[2]" + RESET + " IP Scanner")
        print(MOR + "[3]" + RESET + " Port Scanner")
        print(MOR + "[4]" + RESET + " Network Tools")
        print(MOR + "[5]" + RESET + " Process Viewer")
        print(MOR + "[6]" + RESET + " Cleaner")
        print(GRAY + "[7]" + RESET + "IP LOGGER")

        print(RED + "[0]" + RESET + " Exit")

        try:
            choice = input("\n>> Select: ").strip()
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit()

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
            april_fools()

        elif choice == "0":
            print(RED + "Shutting down HYPER TOOL..." + RESET)
            break

        else:
            print(RED + "Invalid option!" + RESET)

        wait()

if __name__ == "__main__":
    menu()