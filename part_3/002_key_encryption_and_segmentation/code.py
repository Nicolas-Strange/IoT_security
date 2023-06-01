from typing import Tuple

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key


def generate_private_key() -> bytes:
    """ method to generate a private key """
    return Fernet.generate_key()


def encrypt(key: bytes) -> Tuple[bytes, bytes]:
    """ method to encrypt a private key """
    # Generate a new RSA key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()

    # Export the public key in PEM format
    pem_public_key = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Serialize the private key to bytes using PEM format
    private_key_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Encrypt the key using the public key
    encrypted_key = public_key.encrypt(
        key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return encrypted_key, private_key_bytes


def decrypt(encrypted_key: bytes, private_key: bytes) -> bytes:
    """ methode to decrypt the private key """
    private_key_object = load_pem_private_key(
        private_key,
        password=None
    )

    decrypted_key = private_key_object.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_key


def run():
    my_private_key = generate_private_key()
    encrypted_private_key, decipher_key = encrypt(key=my_private_key)
    decrypted_key = decrypt(encrypted_key=encrypted_private_key, private_key=decipher_key)

    print(f"my private key: {my_private_key}")
    print(f"my encrypted private key: {encrypted_private_key}")
    print(f"my decipher private key: {decipher_key}")
    print(f"my decrypted private key: {decrypted_key}")


if __name__ == '__main__':
    run()
