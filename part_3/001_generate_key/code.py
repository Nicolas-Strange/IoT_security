from cryptography.fernet import Fernet

# Generate a new key
key = Fernet.generate_key()

# Store the key securely
# You can save it to a file or use a key management system
# Here, we will simply print it
print("Generated Key:", key)

# Encrypt the key using a public key
# Replace 'public_key' with the actual public key
encrypted_key = public_key.encrypt(key.encode())

# Store the encrypted key securely
# You can save it to a file or use a key management system
# Here, we will simply print it
print("Encrypted Key:", encrypted_key)
