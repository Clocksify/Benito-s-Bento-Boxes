from Crypto.Cipher import AES 
from Crypto import Random
from Crypto.Hash import SHA256
import json
from Crypto.Util.Padding import unpad
from Crypto.Util.Padding import pad

with open("my key.txt", "r") as secrets_file:
    key = secrets_file.readline().strip().encode('utf-8')

    if len(key) < 32:
        hash_key = key.ljust(32, b'\0')

    if len(key) > 32:
        hash_key = key [:32]

s = int(input("What is your starting range? "))

e = int(input("What is your ending range? "))

e_cipher = AES.new(hash_key, AES.MODE_CTR, nonce = iv)
d_cipher = AES.new(hash_key, AES.MODE_CTR, nonce = iv)

EQ_to_EQR_dict = {}

for i in range(s-1, e):
    EQR = list(EQ_to_EQR_dict.values())[i]
    for i in range(len(EQR)):
        plaintext = unpad(d_cipher.decrypt(EQR[i]), AES.block_size)
