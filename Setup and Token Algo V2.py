from Crypto.Cipher import AES 
from Crypto import Random
import chardet
from Crypto.Hash import SHA256
import json

with open("my key.txt", "r") as secrets_file:
    key = secrets_file.readline().strip().encode('utf-8')

    if len(key) < 32:
        hash_key = key.ljust(32, b'\0')

    if len(key) > 32:
        hash_key = key [:32]

iv = Random.get_random_bytes(10)

engine = AES.new(hash_key, AES.MODE_CTR, nonce = iv,)

EQ_to_EQR_dict = {}

for i in range(1, 4):
    with open(f"attr{i}.txt", "r") as name:
        file_lines = bytes(f"attr{i}".read() , 'utf-8').splitlines()
        enc_file = engine.encrypt(f"file{i}")
        enc_decoded = f"enc_file{i}".decode('utf-8')
        print (f"enc_file{i}_str")
        print (hash_key)
# Expected output is Password123 with 0s added at the end until the object is 32 bytes long

    with open(f"attr{i}.txt") as name:
        name = bytes(f"attr{i}".read() , 'utf-8')
        hash = SHA256.new(data = f"attr{i}")
        hash_attr = hash.hexdigest()
        print (f"hash_attr{i}")

#Expected outputs for hash_attr1,2 and 3 are separate and unique 32 byte long digests
    EQ_to_EQR_dict[hash_attr] = str(enc_decoded)

with open("EQ_to_EQR_dict.json", "w") as EQ_to_EQR_dict_dest:
    EQ_to_EQR_dict = EQ_to_EQR_dict_dest.write(json.dumps(EQ_to_EQR_dict))
