import json
import socket
import time

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from flask import Flask, request
from gevent.pywsgi import WSGIServer

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


class SecureCommunication:
    """ class to encrypt and decrypt a message in asymmetric manner """
    def __init__(self):
        self._private_key = None
        self._public_key = None
        self._peer_public_key = None
        self._generate_key_pair()

    @property
    def public_key(self):
        """ get the public key """
        return self._public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    def _generate_key_pair(self) -> None:
        """ generate the pair private and public key """
        self._private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self._public_key = self._private_key.public_key()

    def set_peer_public_key(self, peer_public_key: str) -> None:
        """ setup the peer public key """
        self._peer_public_key = serialization.load_pem_public_key(
            peer_public_key.encode(), backend=default_backend()
        )

    def encrypt_message(self, message: str) -> bytes:
        """ encrypt the message via the peer public key """
        message = {
            "from": HOST, "port": PORT,
            "message": message,
            "nonce": time.time()  # a nonce to avoid the detection of similar messages
        }
        message = json.dumps(message).encode()

        encrypted_message = self._peer_public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        decrypted_message = self._private_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted_message


communication = SecureCommunication()


@app.route('/public-key', methods=['GET'])
def get_public_key():
    """ request to get the server public key """
    return communication.public_key


@app.route('/decrypt-message', methods=['POST'])
def decrypt_received_message():
    encrypted_message = request.get_data()
    print(encrypted_message)
    decrypted_message = communication.decrypt_message(encrypted_message)
    decrypted_message = json.loads(decrypted_message)

    # Do the logic here when a message is received
    print(decrypted_message)

    return "200"


if __name__ == '__main__':
    http_server = WSGIServer((HOST, PORT), app)
    http_server.serve_forever()
