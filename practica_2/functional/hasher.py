from Crypto.Hash import SHA256

from utils.constants import *
from utils.file_manager import *


class Hasher:
    """Class in charge of creating and validating the SHA256 hashing function"""

    def __init__(self):
        """Create a new hasher"""
        self.hash = SHA256.new()

    def get_text_hash(self, text):
        """Update de hasher and return the outcome as text"""
        self.hash.update(text.encode('utf-8'))
        return self.hash.hexdigest()

    def get_hash(self, text):
        """Update de hasher and return the outcome as binary"""
        self.hash.update(text.encode('utf-8'))
        return self.hash

    def check_hash(self, text, shasum):
        """Check if a text and its hash are equal"""
        assert self.get_text_hash(text) == shasum, text_hash_KO
        print(text_hash_OK)


def get_hash(args):
    """Interface to get the file content and hash it into a file"""
    hasher = Hasher()
    text = read_file(args.input)
    shasum = hasher.get_text_hash(text)
    write_binary_file(args.output, shasum)


def check_hash(args):
    """Interface to get the file content and a hash and verify them"""
    hasher = Hasher()
    text = read_file(args.input)
    shasum = read_binary_file(args.additional_input)
    hasher.check_hash(text, shasum)
