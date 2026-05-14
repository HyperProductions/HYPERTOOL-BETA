import requests

def run():
    print("\n=== DISCORD TOOLS ===\n")
    print("[1] Webhook Message Sender")
    print("[2] Server Invite Info")

    choice = input("\nSeçim: ")

    if choice == "1":
        webhook_sender()
    elif choice == "2":
        invite_info()
    else:
        print("Geçersiz seçim!")

def webhook_sender():
    print("\n=== WEBHOOK SENDER ===")
    url = input("Webhook URL: ")
    message = input("Mesaj: ")

    data = {
        "content": message
    }

    try:
        r = requests.post(url, json=data)

        if r.status_code == 204 or r.status_code == 200:
            print("Mesaj gönderildi ✔")
        else:
            print("Hata oluştu:", r.status_code)

    except Exception as e:
        print("Bağlantı hatası:", e)

def invite_info():
    code = input("Discord invite kodu (örn: abc123): ")

    url = f"https://discord.com/api/v10/invites/{code}?with_counts=true"

    try:
        r = requests.get(url)
        data = r.json()

        if "guild" not in data:
            print("Geçersiz invite!")
            return

        print("\n=== SERVER INFO ===")
        print("Server:", data["guild"]["name"])
        print("Members:", data["approximate_member_count"])
        print("Online:", data["approximate_presence_count"])

    except Exception as e:
        print("Hata:", e)