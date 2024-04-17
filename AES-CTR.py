# this code uses AES-CTR
# CTR allows AES to accept data of any length
import json
from Crypto.Cipher import AES 
from Crypto import Random
import base64

with open("my key.txt", "r") as secrets_file:
    key = secrets_file.readline().strip().encode('utf-8')

    if len(key) < 32:
        key = key.ljust(32, b'\0')

    if len(key) > 32:
        key = key [:32]
# 32 bytes is 256 bits
        
with open("plaintext.txt", "r") as plaintext:
    plaintext = bytes(plaintext.read() , 'utf-8')
    plaintext_lines = plaintext.splitlines()
    
iv = Random.get_random_bytes(8)
print (iv)

with open("iv.txt", "wb") as iv_dest:
    iv_dest.write(iv)

engine = AES.new(key, AES.MODE_CTR, initial_value = iv)
ciphertext = engine.encrypt(plaintext)
print (ciphertext)
print (type(ciphertext))

with open("ciphertext.txt", "wb") as ciphertext_dest:
    ciphertext_dest.write(ciphertext)
