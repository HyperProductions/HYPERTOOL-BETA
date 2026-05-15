import os
import socket


def run():
    print("\n=== NETWORK TOOLS ===\n")

    print("[1] Ping Test")
    print("[2] Internet Check")
    print("[3] DNS Lookup")

    choice = input("\nSeçim: ")

    if choice == "1":
        ping_test()

    elif choice == "2":
        internet_check()

    elif choice == "3":
        dns_lookup()

    else:
        print("Geçersiz seçim!")
        input("\nPress Enter...")


def ping_test():
    target = input("Ping atılacak IP / site: ")

    print(f"\n{target} ping atılıyor...\n")

    # ✅ TERMUX/LINUX FIX
    os.system(f"ping -c 4 {target}")

    input("\nPress Enter...")


def internet_check():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)

        print("\nİnternet VAR ✔")

    except Exception as e:

        print("\nİnternet YOK ✖")
        print("Error:", e)

    input("\nPress Enter...")


def dns_lookup():
    domain = input("Domain gir (örnek: google.com): ")

    try:
        ip = socket.gethostbyname(domain)

        print(f"\n{domain} -> {ip}")

    except Exception as e:

        print("DNS çözümlenemedi!")
        print("Error:", e)

    input("\nPress Enter...")