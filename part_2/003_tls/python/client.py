import requests

HOST = "192.168.3.14"
PORT = 38440
url = f"https://{HOST}:{PORT}/logic"  # Replace with the server's IP and port

try:
    response = requests.post(url, verify="client.crt")
    if response.status_code == 200:
        print("Server response:", response.text)
    else:
        print("Request failed with status code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)

