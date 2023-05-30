import requests
from Crypto.PublicKey import RSA

# Server public key
serverPublicKey = "<SERVER_PUBLIC_KEY>"  # Replace with the server's public key

# Load the server's public key
publicKey = RSA.import_key(serverPublicKey)

# Message to be encrypted
message = "Hello from the client"

# Encrypt the message using the server's public key
encryptedMessage = publicKey.encrypt(message.encode(), None)[0].hex()

# Send the encrypted message to the Arduino device
response = requests.post("<ARDUINO_DEVICE_URL>", data=encryptedMessage)

print(response.text)  # Print the response from the Arduino device
