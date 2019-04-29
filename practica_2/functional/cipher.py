from Crypto.Cipher import AES
from Crypto import Random
import base64
import hashlib

from utils.file_manager import *


class Cipher:
    """Class in charge of encrypting the file and decryipting it latter"""

    def __init__(self, key):
        """Generate the key from the passphrase"""
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        """Encrypts the raw input with the previously selected passphrase"""
        # Pad the input
        raw = self._pad(raw)
        # Get a random block, and create a cipher
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        # Return the crypted binary output with the random block
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        """Decrypt the crypted input with the previously selected passphrase"""
        # Decode the encrypted text
        enc = base64.b64decode(enc)
        # Extract the random block and create a cipher
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        # Retrun the decrypted outcome
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, string):
        """String padder"""
        return string + (self.bs - len(string) % self.bs) * chr(self.bs - len(string) % self.bs)

    @staticmethod
    def _unpad(string):
        """String unpadder"""
        return string[:-ord(string[len(string) - 1:])]


def encrypt(args):
    """Interface to get the file content and encrypt it"""
    cipher = Cipher(args.password)
    text = read_file(args.input)
    cryp = cipher.encrypt(text)
    write_binary_file(args.output, cryp)


def decrypt(args):
    """Interface to get the crypted file content and decrypt it"""
    cipher = Cipher(args.password)
    cryp = read_binary_file(args.input)
    text = cipher.decrypt(cryp)
    write_file(args.output, text)
