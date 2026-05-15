import os
import platform
import subprocess

def run():

    print("\n=== TRACEROUTE TOOL ===\n")

    target = input("Domain / IP gir: ")

    try:
        system = platform.system().lower()

        print(f"\nTracing route to {target}...\n")

        # Windows
        if system == "windows":
            os.system(f"tracert {target}")

        # Linux / Termux
        else:
            # Termux'ta traceroute yoksa ping ile fallback
            result = subprocess.run(
                ["traceroute", target],
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                print("\nTraceroute yok, ping fallback çalışıyor...\n")
                os.system(f"ping -c 4 {target}")
            else:
                print(result.stdout)

    except Exception as e:
        print("\nError running traceroute:", e)

    input("\nPress Enter...")