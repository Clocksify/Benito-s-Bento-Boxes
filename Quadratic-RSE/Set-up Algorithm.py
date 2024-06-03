from Crypto.Cipher import AES 
from Crypto import Random
from Crypto.Hash import SHA256
import json
from Crypto.Util.Padding import unpad
from Crypto.Util.Padding import pad

with open("Benito-s-Bento-Boxes/Quadratic-RSE/my_key.txt", "r") as secrets_file:
    key = secrets_file.readline().strip().encode('utf-8')

    if len(key) < 32:
        hash_key = key.ljust(32, b'\0')

    if len(key) > 32:
        hash_key = key [:32]

iv_dict = {}

for i in range(1, 4):
    with open(f"file{i}.txt", "r") as name:
        name_str = str(name)
        f"file{i}_attr" = re.findall('\d+\.\d+|\d+', name_str)
        for j in range(1, 4):
            if f"file{i}_attr" = j:
                f"file{j}" += f"file{i}.txt"

hash_query_to_enc_file_dict = {}

for a in range(4):
    for b in range(4):
        while a <= b:
            query = f"{a},{b}"
            hash = SHA256.new(data = bytes(query, 'utf-8'))
            hash_query = hash.hexdigest()
            for j in range(a, b+1):
                with open(f"file{a},{b}", "w+") as name2:
                    with open(f"file{j}", "r") as name3:
                        name2.write(str(name3))
                        name2 = name2.readline().strip().encode('utf-8')
                        e_cipher = AES.new(hash_key, AES.MODE_CBC)
                        ciphertext = e_cipher.encrypt(pad(name2, AES.block_size))
                        iv = e_cipher.iv
                        iv_dict[f"{a},{b}"] = iv
                        hash_query_to_enc_file_dict[hash_query] = [ciphertext] 
    
hash_query_to_enc_file_dict_final = {}

for key, value in hash_query_to_enc_file_dict.items():
    str_key = str(key)
    str_list = []
    for i in range(len(value)):
        str_value = str(value[i])
        str_list.append(str_value)
    hash_query_to_enc_file_dict_final[str_key] = str_list
    
with open("hash_query_to_enc_file_dict.json", "w") as hash_query_to_enc_file_dict_dest:
    hash_query_to_enc_file_dict_final = hash_query_to_enc_file_dict_dest.write(json.dumps(hash_query_to_enc_file_dict_final))
#Expected output is a json file EQ_to_EQR_dict.json where there are 3 separate 32 byte hashes that are attr1,2 and 3 respectively
#However, no files are in the json file's dictionary output
