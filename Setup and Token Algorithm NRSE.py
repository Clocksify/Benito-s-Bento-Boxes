from Crypto.Cipher import AES 
from Crypto import Random
from Crypto.Hash import KMAC256
import json

with open("file1.txt", "r") as file1:
    file1 = bytes(file1.read() , 'utf-8')
    file1_lines = file1.splitlines()

with open("my key.txt", "r") as secrets_file:
    key = secrets_file.readline().strip().encode('utf-8')

    if len(key) < 32:
        key = key.ljust(32, b'\0')

    if len(key) > 32:
        key = key [:32]

iv = Random.get_random_bytes(10)

engine = AES.new(key, AES.MODE_CTR, nonce = iv,)

enc_file1 = engine.encrypt(file1)
with open("enc_file1.txt", "wb") as enc_file1_dest:
    enc_file1_dest.write(enc_file1)

with open("my key.txt", "r") as secrets_file:
    hash_key = secrets_file.readline().strip().encode('utf-8')

    if len(hash_key) < 32:
        hash_key = hash_key.ljust(32, b'0')

    if len(hash_key) > 32:
        hash_key = hash_key [:32]

print (hash_key)
# Expected output is Password123 with 0s added at the end until the object is 32 bytes long
# KMAC256 provides a security strength of 256 bits. Key is 32 bytes or more

mac = KMAC256.new(key=hash_key, mac_len=8)
print (mac.hexdigest)

mac.update(b'1')
print (mac.hexdigest(b'2'))


with open("attr1.txt", "r") as attr1:
    attr1 = mac.hexdigest()
    print (attr1)

with open("attr2.txt", "r") as attr2:
    attr2 = mac.hexdigest()
    print (attr2)

#Query range is 1-3
EQ_to_EQR_dict = {
    attr1: "file1",
    attr2: "file2"
} 


with open("EQ_to_EQR_dict.json", "w") as EQ_to_EQR_dict_dest:
    EQ_to_EQR_dict = EQ_to_EQR_dict_dest.write(json.dumps(EQ_to_EQR_dict))


