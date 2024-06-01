from Crypto.Cipher import AES 
from Token_Algorithm.py import start_int, end_int
from Setup_Algorithm.py import iv_dict

with open("Benito-s-Bento-Boxes/NRSE/my_key.txt", "r") as secrets_file:
    key = secrets_file.readline().strip().encode('utf-8')

    if len(key) < 32:
        hash_key = key.ljust(32, b'\0')

    if len(key) > 32:
        hash_key = key [:32]

with open('Benito-s-Bento-Boxes/NRSE/iv.txt','rb') as f:
    iv = f.readline()

open("Benito-s-Bento-Boxes/NRSE/Answer.txt",'w').close()

with open("Benito-s-Bento-Boxes/NRSE/Response.txt") as j:
  with open("Benito-s-Bento-Boxes/NRSE/Answer.txt",'w') as g:
    for line in j:
            ciphertextline = line.rstrip()
            stripped = (ciphertextline[2:-1])
            encrypted_response = bytes(stripped,'utf-8')
            decoded_response = encrypted_response.decode('unicode-escape').encode('ISO-8859-1')
            d_iv= iv_dict[start_int]
            d_cipher = AES.new(hash_key, AES.MODE_CBC, d_iv)
            decrypted_response = unpad(d_cipher.decrypt(decoded_response), AES.block_size)
            my_ans = str(decrypted_response)[2:-1]
            g.write(my_ans+'\n')
            start_int += 1

#b'\xed*V\x9fk\x97\xd0\x16\xbdq\xab~\xd9v\xab"y\x98\x95\xb5\xd3\\\xba'
#b'\\xed*V\\x9fk\\x97\\xd0\\x16\\xbdq\\xab~\\xd9v\\xab"y\\x98\\x95\\xb5\\xd3\\\\\\xba'
#b'\\xed*V\\x9fk\\x97\\xd0\\x16\\xbdq\\xab~\\xd9v\\xab\"y\\x98\\x95\\xb5\\xd3\\\\\\xba'
