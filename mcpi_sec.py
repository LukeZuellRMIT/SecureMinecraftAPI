from mcpi.minecraft import Minecraft
import rsa_methods_orig
# Assignment 3 main file
# Feel free to modify, and/or to add other modules/classes in this or other files

# mc = Minecraft.create()
# mc.postToChat("Hello world")

rsa_methods_orig.generateKeys()
#load in keys that were generated
publicKey, privateKey = rsa_methods_orig.loadKeys()
#get the message
message = input('Write your message here:')
#encrypt the message
ciphertext = rsa_methods_orig.encrypt(message, publicKey)
#sign the ciphertext
# signature = rsa_methods.sign(ciphertext, privateKey)
rsa_methods_orig.sign(ciphertext, privateKey)
with open('keys/signature.txt', 'rb') as p:
    signature = p.read()
#decrypt the ciphertext
text = rsa_methods_orig.decrypt(ciphertext, privateKey)

print(f'Cipher text: {ciphertext}')
print(f'Signature: {signature}')


if text:
    print(f'Message text: {text}')
else:
    print(f'Unable to decrypt the message.')

if rsa_methods_orig.verify(ciphertext, signature, publicKey):
    print("Successfully verified signature")
else:
    print('The message signature could not be verified')