from mcpi.minecraft import Minecraft
from mcpi.minecraft import Connection
import rsa_methods


class PostChatExtended(Minecraft):
    
    def postToChatSecure(self, originalMessage):
    
        # Assignment 3 main file
        # Feel free to modify, and/or to add other modules/classes in this or other files

        # mc = Minecraft.create()
        # mc.postToChat("Hello world")
        rsa_instance = rsa_methods.RSAobject()
        rsa_instance.generateKeys()
        #load in keys that were generated
        publicKey, privateKey = rsa_instance.loadKeys()
        #get the message
        #message = input('Write your message here:')
        message = originalMessage
        #encrypt the message
        ciphertext = rsa_instance.encrypt(message, publicKey)
        print('cipher size', len(ciphertext))
        #sign the ciphertext
        hmac = rsa_instance.hmac(ciphertext)
        print('signiture size', len(hmac))
        #encryptedMessage = "Test"
        print(ciphertext)
        print(hmac)
        self.postToChat(ciphertext + hmac)
        
    def create(address = "localhost", port = 4711):
        return PostChatExtended(Connection(address, port))
