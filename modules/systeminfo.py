import platform
import os

def run():
    print("\n=== SYSTEM INFO ===\n")
    print("OS:", platform.system())
    print("Version:", platform.version())
    print("Machine:", platform.machine())
    print("Processor:", platform.processor())
