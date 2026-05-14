import socket

def run():
    print("\n=== PORT SCANNER ===")

    target = input("Hedef IP / Domain: ")

    try:
        start_port = int(input("Başlangıç portu: "))
        end_port = int(input("Bitiş portu: "))
    except ValueError:
        print("Geçersiz port numarası!")
        return

    print(f"\nTaranıyor: {target}\n")

    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)

        sock.close()

    print("\n=== SONUÇ ===")
    if open_ports:
        print("Açık portlar:", open_ports)
    else:
        print("Açık port bulunamadı.")

    print("================\n")