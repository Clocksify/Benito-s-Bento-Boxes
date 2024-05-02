# this code uses AES-CTR
# CTR allows AES to accept data of any length
from Crypto.Cipher import AES 
from Crypto import Random

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
    
iv = Random.get_random_bytes(10)
# iv can be 0 to 15 bytes long
# iv and counter are 16 bytes long together
print (iv)

with open("iv.txt", "wb") as iv_dest:
    iv_dest.write(iv)

engine = AES.new(key, AES.MODE_CTR, nonce = iv,)
ciphertext = engine.encrypt(plaintext)
print (ciphertext)

print (type(ciphertext))

with open("ciphertext.txt", "wb") as ciphertext_dest:
    ciphertext_dest.write(ciphertext)
