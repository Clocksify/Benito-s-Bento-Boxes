from Crypto.Cipher import AES 
from Crypto import Random
from Crypto.Hash import SHA256
import json
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
        name = f"attr{i}".encode('utf-8')
        hash = SHA256.new(data = name)
        hash_attr = hash.hexdigest()
        print (hash_attr)

    for i in range(1, 4):
        with open(f"file{i}.txt", "r") as name:
            file_bytes = f"file{i}".encode('utf-8')
            enc_file = engine.encrypt(file_bytes)
            enc_file = str(enc_file)
            print (enc_file)
            file_list = []

            if hash_attr in enc_file: 
                file_list.append(str(enc_file))
    
    EQ_to_EQR_dict[hash_attr] = file_list


s = int(input("What is your starting range? "))

e = int(input("What is your ending range? "))

for i in range(s-1, e):
    EQR = list(EQ_to_EQR_dict.values())[i]
    for i in range(len(EQR)):
        plaintext = unpad(engine.decrypt(EQR[i]), AES.block_size)
        print(plaintext)
        print("\n")


with open("EQ_to_EQR_dict.json", "w") as EQ_to_EQR_dict_dest:
    EQ_to_EQR_dict = EQ_to_EQR_dict_dest.write(json.dumps(EQ_to_EQR_dict))
#Expected output is a json file EQ_to_EQR_dict.json where there are 3 separate 32 byte hashes that are attr1,2 and 3 respectively
#However, no files are in the json file's dictionary output