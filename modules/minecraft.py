import socket
import os

def run():
    print("\n=== MINECRAFT TOOLS ===\n")
    print("[1] Server Status Check")
    print("[2] Server Ping")
    print("[3] Localhost Check")

    choice = input("\nSeçim: ")

    if choice == "1":
        server_status()
    elif choice == "2":
        server_ping()
    elif choice == "3":
        localhost_check()
    else:
        print("Geçersiz seçim!")

def server_status():
    server = input("Server IP / Domain: ")

    try:
        ip = socket.gethostbyname(server)
        print(f"\nServer DNS OK ✔ -> {ip}")
        print("Not: Gerçek online/offline kontrol için port 25565 gerekir.")
    except:
        print("Server çözümlenemedi!")

def server_ping():
    server = input("Server IP: ")
    print(f"\n{server} ping atılıyor...\n")
    os.system(f"ping {server}")

def localhost_check():
    print("\nLocal Minecraft Server kontrolü...")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        result = s.connect_ex(("127.0.0.1", 25565))

        if result == 0:
            print("Local Minecraft Server AÇIK ✔")
        else:
            print("Local Minecraft Server KAPALI ✖")

        s.close()
    except:
        print("Hata oluştu!")