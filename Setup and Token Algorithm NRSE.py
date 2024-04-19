from Crypto.Cipher import AES 
from Crypto import Random
import chardet
from Crypto.Hash import SHA256
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
print (type(enc_file1))
print (enc_file1)

with open("enc_file1.txt", "wb") as enc_file1_dest:
    enc_file1_dest.write(enc_file1)

enc_file1_str = enc_file1.decode('utf-8')
print (enc_file1_str)

with open("my key.txt", "r") as secrets_file:
    hash_key = secrets_file.readline().strip().encode('utf-8')

    if len(hash_key) < 32:
        hash_key = hash_key.ljust(32, b'0')

    if len(hash_key) > 32:
        hash_key = hash_key [:32]

print (hash_key)
# Expected output is Password123 with 0s added at the end until the object is 32 bytes long

with open("attr1.txt", "r") as attr1:
    attr1 = bytes(attr1.read() , 'utf-8')
    hash = SHA256.new(data = attr1)
    hash_attr1 = hash.hexdigest()
    print (hash_attr1)

with open("attr2.txt", "r") as attr2:
    attr2 = bytes(attr2.read() , 'utf-8')
    hash = SHA256.new(data = attr2)
    hash_attr2 = hash.hexdigest()
    print (hash_attr2)

with open("attr3.txt", "r") as attr3:
    attr3 = bytes(attr3.read() , 'utf-8')
    hash = SHA256.new(data = attr3)
    hash_attr3 = hash.hexdigest()
    print (hash_attr3)
#Expected outputs for hash_attr1,2 and 3 are separate and unique 32 byte long digests

#Query range is 1-3
EQ_to_EQR_dict = {
    hash_attr1: enc_file1_str,
    hash_attr2: "file_2",
    hash_attr3: "file_3"
} 


with open("EQ_to_EQR_dict.json", "w") as EQ_to_EQR_dict_dest:
    EQ_to_EQR_dict = EQ_to_EQR_dict_dest.write(json.dumps(EQ_to_EQR_dict))


