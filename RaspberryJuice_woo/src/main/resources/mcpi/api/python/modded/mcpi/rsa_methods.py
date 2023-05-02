from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import HMAC, SHA256
from Crypto.Hash import SHA256
import hmac
import hashlib
import base64

#pip install pycryptodome

class RSAobject:
    def __init__(self):
        self.pubKey = 'none'
        self.keyPair = 'none'
        
    def generateKeys(self):
        #using RSA-2048 as specified in phase 2.2
        self.keyPair = RSA.generate(2048)
        self.pubKey = self.keyPair.publickey()
        pubKeyPEM = self.pubKey.exportKey(format='PEM')
        with open('RaspberryJuice_woo/src/main/resources/mcpi/api/python/modded/mcpi/publicKey.pem', 'wb') as p:
            p.write(pubKeyPEM)
        privKeyPEM = self.keyPair.exportKey(format='PEM',pkcs=8)
        with open('RaspberryJuice_woo/src/main/resources/mcpi/api/python/modded/mcpi/privateKey.pem', 'wb') as p:
            p.write(privKeyPEM)
            
    def loadKeys(self):
        return self.pubKey, self.keyPair

    def encrypt(self, message, key):
        encryptor = PKCS1_OAEP.new(key)
        encrypted = encryptor.encrypt(message.encode('utf-8'))
        return encrypted

    def decrypt(self, ciphertext, key):
        try:
            decryptor = PKCS1_OAEP.new(key)
            decrypted = decryptor.decrypt(ciphertext)
            return decrypted
        except:
            return False
        
    def sign(self, message, key):
        signer = pkcs1_15.new(key)
        hasher = SHA256.new()
        hasher.update(message)
        signature = signer.sign(hasher)
        return signature
    
    #AUTH using SHA-256 as specified in phase 2.2
    def hmac(self, message):
        h = HMAC.new(self.keyPair.exportKey(), digestmod=SHA256)
        h.update(message)
        return h.digest()
    
    
    # def create_hash(self, key, message, algorithm):
    #     # secret_bytes = bytes(key, "utf-8")
    #     # payload_bytes = bytes(message, "utf-8")
    #     return hmac.new(key, msg=message, digestmod=algorithm).digest()


    # def hash_and_convert_to_base64_string(self, key, message, algorithm):
    #     hash_obj = self.create_hash(key, message, algorithm)
    #     return base64.b64encode(hash_obj).decode("utf-8").strip()


    # secret_key = "This is the secret"
    # hash_message = "This is the hash message"
    # print(hash_and_convert_to_base64_string(secret_key, hash_message, hashlib.sha256))

    # def verify(self, message, signature, key):
    #     try:
    #         return rsa.verify(message, signature, key,) == 'SHA-256'
    #     except:
    #         return False
