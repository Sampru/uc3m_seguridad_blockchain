from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

from functional.hasher import Hasher
from utils.file_manager import *
from utils.constants import *


class Signer:
    """Class in charge of signing the file and validating the signature"""

    def __init__(self):
        """Instantiates the hashing object, and gets the keys"""
        self.hasher = Hasher()
        self.private_key, self.public_key = get_keys()

    def sign(self, text):
        """Sings a text hash, and returns the signature"""
        # Get the key
        key = RSA.importKey(open(self.private_key).read())
        # Calculate text hash
        shasum = self.hasher.get_hash(text)
        # Sign the hash
        signer = PKCS1_v1_5.new(key)
        return signer.sign(shasum)

    def check_sign(self, text, signature):
        """Checks if a signature matches its remitent"""
        # Get the key
        key = RSA.importKey(open(self.public_key).read())
        # Calculate text hash
        shasum = self.hasher.get_hash(text)
        # Verify that they match
        verifier = PKCS1_v1_5.new(key)
        assert verifier.verify(shasum, signature), text_signature_KO
        print(text_signature_OK)


def sign(args):
    """Interface to get the file content and sign it"""
    signer = Signer()
    text = read_file(args.input)
    signature = signer.sign(text)
    write_binary_file(args.output, signature)


def check_sign(args):
    """Interface to get the file content and verify it with the sign"""
    signer = Signer()
    text = read_file(args.input)
    signature = read_binary_file(args.additional_input)
    signer.check_sign(text, signature)
