from cryptography.fernet import Fernet

# Generate a new encryption key
encryption_key = Fernet.generate_key()

# Initialize the Fernet cipher with the encryption key
cipher = Fernet(encryption_key)

# Part of code to be encrypted
sensitive_data = """
def calculate_sum(a, b):
    result = a + b
    return result

print(calculate_sum(2, 3))
"""

# Encrypt the sensitive data
encrypted_data = cipher.encrypt(sensitive_data.encode())

# Save the encrypted data to a file
with open("encrypted_data.txt", "wb") as file:
    file.write(encrypted_data)

# Decrypt the encrypted data
with open("encrypted_data.txt", "rb") as file:
    encrypted_data = file.read()

decrypted_data = cipher.decrypt(encrypted_data).decode()
print(decrypted_data)
