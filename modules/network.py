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

def ping_test():
    target = input("Ping atılacak IP / site: ")

    print(f"\n{target} ping atılıyor...\n")
    os.system(f"ping {target}")

def internet_check():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        print("\nİnternet VAR ✔")
    except:
        print("\nİnternet YOK ✖")

def dns_lookup():
    domain = input("Domain gir (örnek: google.com): ")

    try:
        ip = socket.gethostbyname(domain)
        print(f"\n{domain} -> {ip}")
    except:
        print("DNS çözümlenemedi!")