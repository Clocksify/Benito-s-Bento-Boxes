from Crypto.Cipher import AES 
from Crypto import Random
from Crypto.Hash import SHA256
import json
from Crypto.Util.Padding import unpad
from Crypto.Util.Padding import pad
import pytest
import numpy as np 
import string

def case(key, start_int, end_int): 
    letters = np.array(list(chr(ord('a') + i) for i in range(26))); letters
    for i in range(1,4):
        n = 1024**2
        text = np.random.choice(letters,n)
        new_text =''.join((text).tolist())
        with open(f"NRSE/file{i}.txt", "w+") as name:
            name.write(new_text)
    if len(key) < 32:
        hash_key = key.ljust(32, b'\0')

    if len(key) > 32:
        hash_key = key [:32]

    iv = Random.get_random_bytes(10)
    with open("NRSE/iv.txt",'wb') as f:
        f.write(iv)
    e_cipher = AES.new(hash_key, AES.MODE_CTR, nonce = iv)
    d_cipher = AES.new(hash_key, AES.MODE_CTR, nonce = iv)

    EQ_to_EQR_dict = {}

    #start_int = int(input("What is your starting range? "))

    #end_int = int(input("What is your ending range? "))

    for i in range(start_int, end_int+1):
        hash = SHA256.new(data = bytes(str(i), 'utf-8'))
        hash_attr = hash.hexdigest()
        with open(f"NRSE/file{i}.txt", "r") as name:
            name = name.readline().strip().encode('utf-8')
            ciphertext = e_cipher.encrypt(name)
            EQ_to_EQR_dict[hash_attr] = [ciphertext]

                # change to if hash_atr in file_bytes with proper use case

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
    with open("NRSE/EQ_to_EQR_dict.json", "w") as EQ_to_EQR_dict_dest:
        EQ_to_EQR_dict_dest.write(json.dumps(EQ_to_EQR_dict_final))
    return(EQ_to_EQR_dict_final)

    #Expected output is a json file EQ_to_EQR_dict.json where there are 3 separate 32 byte hashes that are attr1,2 and 3 respectively
    #However, no files are in the json file's dictionary output
    
def test_case():
    with open('my_key.txt', 'r') as j:
        key = j.readline().strip().encode('utf-8')
        Answer = case(key, 1,2)
        print(Answer)
    with open('NRSE/EQ_to_EQR_dict.json','r') as j:
        Answer2 = json.load(j)
        print(Answer2)
    assert Answer == Answer2
