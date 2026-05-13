import os
from modules import systeminfo, ipscanner, portscanner, network, processviewer, cleaner

MOR = "\033[95m"
SIFIR = "\033[0m"
KALIN = "\033[1m"
GRI = "\033[90m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    print(MOR + KALIN)
    print(r"""

               H Y P E R   T O O L
""")
    print(SIFIR)

def menu():
    while True:
        clear()
        banner()

        print(MOR + "[1]" + SIFIR + " System Information")
        print(MOR + "[2]" + SIFIR + " IP Scanner")
        print(MOR + "[3]" + SIFIR + " Port Scanner")
        print(MOR + "[4]" + SIFIR + " Network Tools")
        print(MOR + "[5]" + SIFIR + " Process Viewer")
        print(MOR + "[6]" + SIFIR + " Cleaner")
        print(GRI + "[0]" + SIFIR + " Exit")

        choice = input("\n>> Select: ")

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
        elif choice == "0":
            print(MOR + "HYPER TOOL shutting down..." + SIFIR)
            break
        else:
            print("Invalid option!")

        input("\nPress Enter...")

menu()