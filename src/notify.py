import requests

API_TOKEN = "CHANGE_ME_before_merge"

def send(message):
    try:
        response = requests.post("https://hooks.example.internal/send", json={"text": message})
        return response.status_code
    except:
        return -1

def placeholder_hook():
    pass
