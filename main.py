import requests
import folium
import time
from pyfiglet import Figlet


def get_info_by_ip(ip):
    try:
        response = requests.get(url=f"http://ip-api.com/json/{ip}").json()

        data = {
            "IP": response.get("query"),
            "COUNTRY": response.get("country"),
            "COUNTRY_CODE": response.get("countryCode"),
            "REGION_NAME": response.get("regionName"),
            "CITY": response.get("city"),
            "ZIP_POSTAL_CODE": response.get("zip"),
            "LAT": response.get("lat"),
            "LON": response.get("lon"),
            "TIMEZONE": response.get("timezone"),
            "INERNET_PROVIDER": response.get("isp"),
            "ORGANIZATION": response.get("org"),
            "ASN": response.get("as"),
        }

        for key, value in data.items():
            print(f"{key} >>> {value}")

        area = folium.Map(location=[data["LAT"], data["LON"]], zoom_start=15)
        folium.Marker(location=[data["LAT"], data["LON"]], icon=folium.Icon(
            color="red", icon="glyphicon-record", iconColor="white")).add_to(area)
        area.save(
            f'{time.strftime("%d-%m-%Y %H;%M.%S")}_{data["CITY"]}_{data["IP"]}.html')

    except requests.exceptions.ConnectionError:
        print("Huston, we`ve got connection troubles!!")


def main():
    preview_text = Figlet(font="slant")
    print(preview_text.renderText("IP_INFO"))
    ip = input("Please, enter IP: ")
    print("-" * 30)
    get_info_by_ip(ip=ip)


if __name__ == '__main__':
    main()
