import requests

from api_communication import SecureCommunication


class MessageSender:
    def __init__(self, server_host: str, server_port: int):
        self._endpoint = f'http://{server_host}:{server_port}'

        self._api_com = SecureCommunication()
        # Get the public keys of the server
        self._server_public_key = requests.get(
            f'{self._endpoint}/public-key'
        ).text
        self._api_com.set_peer_public_key(self._server_public_key)

    def send_message(self, message: str) -> str:
        """ encrypt the message with the public key provided by the server """
        encrypted_message = self._api_com.encrypt_message(message)
        response = requests.post(
            f'{self._endpoint}/decrypt-message',
            data=encrypted_message
        ).text

        if response == "200":
            return "message delivered"

        return "error"


def run():
    message_sender = MessageSender(server_host="192.168.3.21", server_port=5000)
    message = "Hello form the client"
    response = message_sender.send_message(message=message)
    print(response)


if __name__ == '__main__':
    run()
