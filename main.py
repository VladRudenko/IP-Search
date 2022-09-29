import requests


def get_info_by_ip(ip):
    try:
        response = requests.get(url=f"http://ip-api.com/json/{ip}").json()
        print(response)
    except requests.exceptions.ConnectionError:
        print("Huston, we have got connection troubles!!")


ip = input("Please, enter IP: ")
get_info_by_ip(ip=ip)
