import requests
from retry import retry

HOST = "192.168.3.21"
PORT = 5000


@retry(tries=3, delay=1, backoff=2)
def auth():
    url = f"http://{HOST}:{PORT}/login"  # Replace with the appropriate URL of the server

    data = {
        "username": "admin",
        "password": "admin123"
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        print("Login successful")
    else:
        print("Invalid credentials")


if __name__ == '__main__':
    auth()
