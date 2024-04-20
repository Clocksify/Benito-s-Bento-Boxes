from Crypto.Cipher import AES 
from Crypto import Random
import chardet
from Crypto.Hash import SHA256
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

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
    with open(f"attr{i}.txt") as name:
        name = bytes(f"attr{i}".read() , 'utf-8')
        hash = SHA256.new(data = name)
        hash_attr = hash.hexdigest()
        print(f"hash_attr{i}")

    for i in range(1, 4):
        with open(f"file{i}.txt", "r") as name:
            file_lines = bytes(f"file{i}".read() , 'utf-8').splitlines()
            enc_file = engine.encrypt(f"file{i}")
            enc_decoded = enc_file.decode('utf-8')
            print(hash_key)

            file_list = []

            if hash_attr in enc_decoded: 
                file_list.append(str(enc_decoded))
    
    EQ_to_EQR_dict[hash_attr] = file_list


s = input("What is your starting range? ")

e = input("What is your ending range? ")

for i in range(s-1, e):
    EQR = EQ_to_EQR_dict.values()[i]
    for i in range(len[EQR]):
        plaintext = unpad(engine.decrypt(EQR[i]), AES.block_size)
        print(plaintext)
        print("\n")

# Expected output is Password123 with 0s added at the end until the object is 32 bytes long

#Expected outputs for hash_attr1,2 and 3 are separate and unique 32 byte long digests


with open("EQ_to_EQR_dict.json", "w") as EQ_to_EQR_dict_dest:
    EQ_to_EQR_dict = EQ_to_EQR_dict_dest.write(json.dumps(EQ_to_EQR_dict))
