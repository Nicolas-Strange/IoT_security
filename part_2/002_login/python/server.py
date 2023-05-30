import json
import socket

from flask import Flask, request, jsonify
from gevent.pywsgi import WSGIServer
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)


def get_ip_address():
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Connect to a public DNS server to retrieve the IP address
        sock.connect(("8.8.8.8", 80))
        ip_address = sock.getsockname()[0]
    finally:
        # Close the socket
        sock.close()

    return ip_address


HOST = get_ip_address()
PORT = 5000

# for the example the passwords are hard coded that is not a good practice
# you must store them in a secure place
users = [
    {"username": "admin", "password": generate_password_hash("admin123")}
]


@app.route("/login", methods=["POST"])
def login() -> json:
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    user = next((user for user in users if user["username"] == username), None)
    if user and check_password_hash(user["password"], password):
        # Your logic when successful login
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Invalid credentials"}), 401


if __name__ == '__main__':
    http_server = WSGIServer((HOST, PORT), app)
    http_server.serve_forever()
