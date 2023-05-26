import hashlib
from typing import Tuple

import rsa
from rsa import PublicKey, PrivateKey, VerificationError


def generate_keys() -> Tuple[PublicKey, PrivateKey]:
    """ generate the private key to sign and the public key to verify """
    public_key, private_key = rsa.newkeys(2048)
    return public_key, private_key


def create_signature(firmware: bytes, private_key: PrivateKey) -> bytes:
    """ generate the signature of the firmware or the code """

    # Calculate the hash
    hash_value = hashlib.sha256(firmware).digest()

    # Sign the hash with the private key
    signature = rsa.sign(message=hash_value, priv_key=private_key, hash_method='SHA-256')

    return signature


def verify(firmware: bytes, signature: bytes, public_key: PublicKey) -> bool:
    """ Verify the authenticity of the firmware """
    hash_value = hashlib.sha256(firmware).digest()
    try:
        rsa.verify(message=hash_value, signature=signature, pub_key=public_key)
        return True
    except VerificationError:
        return False


def run():
    """ core function to create the sign a code or a firmware """
    official_firmware = b"This is the firmware."
    altered_firmware = b"This is the altered firmware."

    # Create the signature of the official firmware on your computer
    public_key, private_key = generate_keys()
    signature = create_signature(firmware=official_firmware, private_key=private_key)

    # Verify the authenticity of the firmware on the IoT device
    verify_official = verify(firmware=official_firmware, signature=signature, public_key=public_key)
    verify_altered = verify(firmware=altered_firmware, signature=signature, public_key=public_key)

    print(f"Is official_firmware official: {verify_official}")
    print(f"Is altered_firmware official: {verify_altered}")


if __name__ == '__main__':
    run()
