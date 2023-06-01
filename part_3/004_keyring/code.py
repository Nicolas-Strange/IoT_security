from subprocess import Popen, PIPE, STDOUT


def store_key_in_keyring(key_label: str, key_value: bytes) -> str:
    """ store the key in the keyring """
    command = ['secret-tool', 'store', f"--label='{key_label}'", "password", key_label]
    p = Popen(command, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    grep_stdout = p.communicate(input=key_value)[0]
    return grep_stdout.decode()


def retrieve_key_from_keyring(key_label: str) -> bytes:
    """ get the key from the keyring """
    command = ['secret-tool', 'lookup', "password", key_label]
    p = Popen(command, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    grep_stdout = p.communicate()[0]

    return grep_stdout


def delete_key(key_label: str) -> str:
    """ delete the key from the keyring """
    command = ['secret-tool', 'clear', "password", key_label]
    p = Popen(command, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    grep_stdout = p.communicate()[0]

    return grep_stdout.decode()


def run():
    # Example usage
    key_label = "My_Key"
    key_value = b"2eDEMAGzPa0XIarQZQhlz5DX3ZiwxHfXODo9rL3hNE8="

    # Store the key in the keyring
    store_key_in_keyring(key_label, key_value)

    # Retrieve the key from the keyring
    retrieved_key = retrieve_key_from_keyring(key_label)

    print("Retrieved Key:", retrieved_key)

    # Delete the key in the keyring
    delete_key(key_label=key_label)


if __name__ == '__main__':
    run()
