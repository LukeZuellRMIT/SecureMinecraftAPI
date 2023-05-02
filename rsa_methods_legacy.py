# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_OAEP
# from Crypto.Signature import pkcs1_15
# from Crypto.Hash import SHA256
# import binascii

# class RSA:
#     def __init__(self):
#         self.pubKey = 'none'
#         self.keyPair = 'none'
        
#     def generateKeys(self):
#         #using RSA-2048 as specified in phase 2.2
#         self.keyPair = RSA.generate(2048)
#         self.pubKey = self.keyPair.publickey()
#         pubKeyPEM = self.pubKey.exportKey(format='PEM')
#         with open('keys/publicKey.pem', 'wb') as p:
#             p.write(pubKeyPEM)
#         privKeyPEM = self.keyPair.exportKey(format='PEM',pkcs=8)
#         with open('keys/privateKey.pem', 'wb') as p:
#             p.write(privKeyPEM)
            
#     def loadKeys(self):
#         return self.pubKey, self.keyPair

#     def encrypt(self, message, key):
#         encryptor = PKCS1_OAEP.new(key)
#         encrypted = encryptor.encrypt(message.encode('utf-8'))
#         with open('keys/encryption.txt', 'wb') as p:
#             p.write(encrypted)
#         return encrypted

#     def decrypt(self, ciphertext, key):
#         try:
#             decryptor = PKCS1_OAEP.new(key)
#             decrypted = decryptor.decrypt(ciphertext)
#             return decrypted
#         except:
#             return False

#     #AUTH using SHA-256 as specified in phase 2.2
#     def sign(self, message, key):
#         signer = pkcs1_15.new(key)
#         hasher = SHA256.new()
#         hasher.update(message)
#         signature = signer.sign(hasher)
#         with open('keys/signature.txt', 'wb') as p:
#             p.write(signature)
#         #return signature

#     # def verify(self, message, signature, key):
#     #     try:
#     #         return rsa.verify(message, signature, key,) == 'SHA-256'
#     #     except:
#     #         return False
    

#     ###### what was in origiinal project
    
# import rsa
# #make sure to run pip install rsa
# #rsa version 4.9

# def generateKeys():
#     #using RSA-2048 as specified in phase 2.2
#     (publicKey, privateKey) = rsa.newkeys(2048)
#     with open('publicKey.pem', 'wb') as p:
#         p.write(publicKey.save_pkcs1('PEM'))
#     with open('privateKey.pem', 'wb') as p:
#         p.write(privateKey.save_pkcs1('PEM'))
        
# def loadKeys():
#     with open('publicKey.pem', 'rb') as p:
#         publicKey = rsa.PublicKey.load_pkcs1(p.read())
#     with open('privateKey.pem', 'rb') as p:
#         privateKey = rsa.PrivateKey.load_pkcs1(p.read())
#     return publicKey, privateKey

# def encrypt(message, key):
#     encryption = rsa.encrypt(message.encode('utf-8'), key)
#     with open('keys/encryption.txt', 'wb') as p:
#         p.write(encryption)
#     return encryption

# def decrypt(ciphertext, key):
#     try:
#         return rsa.decrypt(ciphertext, key).decode('utf-8')
#     except:
#         return False

# #AUTH using SHA-256 as specified in phase 2.2
# def sign(message, key):
#     return rsa.sign(message, key, 'SHA-256')

# def verify(message, signature, key):
#     try:
#         return rsa.verify(message, signature, key,) == 'SHA-256'
#     except:
#         return False
    

    

