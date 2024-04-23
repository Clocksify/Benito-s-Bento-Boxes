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

iv = Random.get_random_bytes(10)

e_cipher = AES.new(hash_key, AES.MODE_CTR, nonce = iv)
d_cipher = AES.new(hash_key, AES.MODE_CTR, nonce = iv)

EQ_to_EQR_dict = {}

for i in range(1, 4):
    with open(f"attr{i}.txt") as name:
        name = f"attr{i}".encode('utf-8')
        hash = SHA256.new(data = name)
        hash_attr = hash.hexdigest()
        #print(hash_attr)
    
    EQ_to_EQR_dict[hash_attr] = []
    for i in range(1, 4):
        with open(f"file{i}.txt", "r") as name:
            ciphertext = e_cipher.encrypt(pad(f"file{i}", AES.block_size))

            # change to if hash_atr in file_bytes with proper use case
            if ciphertext not in EQ_to_EQR_dict[hash_attr]: 
                EQ_to_EQR_dict[hash_attr].append(ciphertext)
        
        print(EQ_to_EQR_dict)

s = int(input("What is your starting range? "))

e = int(input("What is your ending range? "))

for i in range(s-1, e):
    EQR = list(EQ_to_EQR_dict.values())[i]
    for i in range(len(EQR)):
        plaintext = unpad(d_cipher.decrypt(EQR[i]), AES.block_size)

# convert all items in dictionary to str
EQ_to_EQR_dict_final = {}
for key, value in EQ_to_EQR_dict.items():
    str_key = str(key)
    str_list = []
    for i in range(len(value)):
        str_value = str(value[i])
        str_list.append(str_value)
    EQ_to_EQR_dict_final[str_key] = str_list

print(EQ_to_EQR_dict_final)
with open("EQ_to_EQR_dict.json", "w") as EQ_to_EQR_dict_dest:
    EQ_to_EQR_dict_final = EQ_to_EQR_dict_dest.write(json.dumps(EQ_to_EQR_dict_final))
#Expected output is a json file EQ_to_EQR_dict.json where there are 3 separate 32 byte hashes that are attr1,2 and 3 respectively
#However, no files are in the json file's dictionary output
