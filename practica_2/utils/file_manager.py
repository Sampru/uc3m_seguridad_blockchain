import os


def read_file(path):
    """Reads the requested file and returns its content as string"""
    with open(path, 'r') as f:
        text = f.read()
    return text


def write_file(path, text):
    """Creates or overwrites the file with the content in the string"""
    with open(path, 'w+') as f:
        f.write(text)
    print('Fichero %s generado' % path)


def read_binary_file(path):
    """Reads the requested file in binary and returns its content as string"""
    with open(path, 'rb') as f:
        text = f.read()
    return text


def write_binary_file(path, text):
    """Creates or overwrites the file with the binary content in the string"""
    with open(path, 'wb+') as f:
        f.write(text)
    print('Fichero %s generado' % path)


def check_file(path):
    """Checks if a file is missing, boolean outcome"""
    return os.path.isfile(path)


def get_keys():
    """Finds a pair of public and private keys in 'files' folder
    Private key file mask: *_rsa
    Public key file mask: *_rsa.pub
    First match
    """
    private_key = None
    public_key = None

    # Iterate 'files' folder to get a file with a matching pattern
    for file in os.listdir("./files"):
        if file.endswith("_rsa") and private_key is None:
            private_key = os.path.join("./files", file)
        if file.endswith("_rsa.pub") and public_key is None:
            public_key = os.path.join("./files", file)

    # Raise an error if there is no key pair
    if private_key is None or public_key is None:
        raise FileNotFoundError

    return private_key, public_key
