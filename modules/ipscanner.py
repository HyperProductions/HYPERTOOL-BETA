import requests

def run():

    print("\n=== IP INFO UPGRADE ===\n")

    ip = input("Enter IP Address: ")

    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data = response.json()

        if data.get("status") != "success":
            print("\n❌ Invalid IP or request failed")
            input("\nPress Enter...")
            return

        print("\n=== BASIC INFO ===\n")
        print("IP:", data.get("query"))
        print("Country:", data.get("country"))
        print("Region:", data.get("regionName"))
        print("City:", data.get("city"))
        print("ZIP:", data.get("zip"))
        print("Timezone:", data.get("timezone"))

        print("\n=== NETWORK INFO ===\n")
        print("ISP:", data.get("isp"))
        print("ORG:", data.get("org"))
        print("AS:", data.get("as"))

        print("\n=== LOCATION ===\n")
        lat = data.get("lat")
        lon = data.get("lon")

        print("Latitude:", lat)
        print("Longitude:", lon)

        # 🔥 GOOGLE MAPS LINK
        if lat and lon:
            print("\nGoogle Maps:")
            print(f"https://www.google.com/maps?q={lat},{lon}")

        print("\n=== STATUS ===")
        print("Query Status:", data.get("status"))

    except Exception as e:
        print("\n❌ Error while fetching IP info")
        print("Error:", e)

    input("\nPress Enter...")