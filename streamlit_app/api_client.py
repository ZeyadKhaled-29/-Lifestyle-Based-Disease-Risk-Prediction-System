import requests

BASE_URL = "http://127.0.0.1:8000"

def predict(endpoint, payload):

    url = f"{BASE_URL}/predict/{endpoint}"

    response = requests.post(url, json=payload)

    # 🔥 DEBUG OUTPUT
    print("STATUS CODE:", response.status_code)
    print("RAW RESPONSE:", response.text)

    return response.json()