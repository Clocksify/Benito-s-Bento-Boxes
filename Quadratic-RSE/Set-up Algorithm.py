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
    with open(f"Benito-s-Bento-Boxes/Quadratic-RSE/file{i}.txt", "r") as name:
        name_str = str(name)
        f"attr{i}" = re.findall('\d+\.\d+|\d+', name_str)
        for j in range(1, 4):
            if f"attr{i}" = j:
                f"file{j}" += f"Benito-s-Bento-Boxes/Quadratic-RSE/file{i}.txt"

hash_query_to_enc_file_dict = {}

for a in range(4):
    for b in range(4):
        while a <= b:
            query = a + ", " + b
            hash = SHA256.new(data = bytes(str(query), 'utf-8'))
            hash_query = hash.hexdigest()
            for j in range(a, b+1):
                f"file{a, b}" += f"file{j}"
                hash_query_to_enc_file_dict[hash_query] = file{a, b}
    
    hash = SHA256.new(data = bytes(str(i), 'utf-8'))
    hash_attr = hash.hexdigest()
    with open(f"Benito-s-Bento-Boxes/NRSE/file{i}.txt", "r") as name:
        name = name.readline().strip().encode('utf-8')
        e_cipher = AES.new(hash_key, AES.MODE_CBC)
        ciphertext = e_cipher.encrypt(pad(name, AES.block_size))
        iv = e_cipher.iv
        iv_dict[i] = iv
        EQ_to_EQR_dict[hash_attr] = [ciphertext]

            # change to if hash_atr in file_bytes with proper use case

'''''
if ciphertext not in EQ_to_EQR_dict[hash_attr]: 
            EQ_to_EQR_dict[hash_attr].append(ciphertext)
            print(EQ_to_EQR_dict)
'''''

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
with open("Benito-s-Bento-Boxes/NRSE/EQ_to_EQR_dict.json", "w") as EQ_to_EQR_dict_dest:
    EQ_to_EQR_dict_final = EQ_to_EQR_dict_dest.write(json.dumps(EQ_to_EQR_dict_final))
#Expected output is a json file EQ_to_EQR_dict.json where there are 3 separate 32 byte hashes that are attr1,2 and 3 respectively
#However, no files are in the json file's dictionary output
