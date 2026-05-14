import requests

def run():

    print("\n=== IP SCANNER ===\n")

    ip = input("Enter IP Address : ")

    try:

        response = requests.get(
            f"http://ip-api.com/json/{ip}"
        )

        data = response.json()

        print("\n=== IP INFORMATION ===\n")

        print("IP Address :", data.get("query"))
        print("Country :", data.get("country"))
        print("Region :", data.get("regionName"))
        print("City :", data.get("city"))
        print("ZIP Code :", data.get("zip"))
        print("ISP :", data.get("isp"))
        print("Timezone :", data.get("timezone"))
        print("Latitude :", data.get("lat"))
        print("Longitude :", data.get("lon"))

    except:

        print("\nError while scanning IP.")