# crypto/rsa_handler.py
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import os


class RSAHandler:
    def __init__(self):
        self.key_dir = "keys"
        os.makedirs(self.key_dir, exist_ok=True)

        self.private_key_path = os.path.join(self.key_dir, "private_key.pem")
        self.public_key_path = os.path.join(self.key_dir, "public_key.pem")

        if not os.path.exists(self.private_key_path) or not os.path.exists(self.public_key_path):
            self._generate_keys()

        self._load_keys()

    def _generate_keys(self):
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()

        with open(self.private_key_path, 'wb') as f:
            f.write(private_key)

        with open(self.public_key_path, 'wb') as f:
            f.write(public_key)

    def _load_keys(self):
        with open(self.private_key_path, 'rb') as f:
            self.private_key = RSA.import_key(f.read())
        with open(self.public_key_path, 'rb') as f:
            self.public_key = RSA.import_key(f.read())

    def encrypt(self, plaintext):
        cipher = PKCS1_OAEP.new(self.public_key)
        encrypted = cipher.encrypt(plaintext.encode('utf-8'))
        return base64.b64encode(encrypted).decode('utf-8')

    def decrypt(self, ciphertext):
        cipher = PKCS1_OAEP.new(self.private_key)
        decrypted = cipher.decrypt(base64.b64decode(ciphertext))
        return decrypted.decode('utf-8')
