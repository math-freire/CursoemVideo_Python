import requests

url = "http://pudim.com.br/"
timeout = 5
try:
    request = requests.get(url, timeout=timeout)
    print("Connected to the Internet")
except (requests.ConnectionError, requests.Timeout) as exception:
    print("No internet connection.")
