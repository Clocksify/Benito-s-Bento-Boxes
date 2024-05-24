from Crypto.Cipher import AES 
from Token_Algorithm.py import start_int, end_int

with open("Benito-s-Bento-Boxes/NRSE/my_key.txt", "r") as secrets_file:
    key = secrets_file.readline().strip().encode('utf-8')

    if len(key) < 32:
        hash_key = key.ljust(32, b'\0')

    if len(key) > 32:
        hash_key = key [:32]

with open('Benito-s-Bento-Boxes/NRSE/iv.txt','rb') as f:
    iv = f.readline()

d_cipher = AES.new(hash_key, AES.MODE_CTR, nonce = iv)

open("Benito-s-Bento-Boxes/NRSE/Answer.txt",'w').close()

with open("Benito-s-Bento-Boxes/NRSE/Response.txt") as j:
  with open("Benito-s-Bento-Boxes/NRSE/Answer.txt",'w') as g:
    for line in j:
      ciphertextline = line.rstrip()
      stripped = (ciphertextline[2:-1])
      encrypted_response = bytes(stripped,'utf-8')
      decoded_response = encrypted_response.decode('unicode-escape').encode('ISO-8859-1')
      decrypted_response = d_cipher.decrypt(decoded_response)
      my_ans = str(decrypted_response)[2:-1]
      g.write(my_ans+'\n')

with open("Benito-s-Bento-Boxes/NRSE/Answer.txt",'r+') as f:
    lines = f.readlines()
    f.seek(0)
    f.truncate()
    for number, line in enumerate(lines):
        if number in [start_int, end_int+1]:
            f.write(line)
#b'\xed*V\x9fk\x97\xd0\x16\xbdq\xab~\xd9v\xab"y\x98\x95\xb5\xd3\\\xba'
#b'\\xed*V\\x9fk\\x97\\xd0\\x16\\xbdq\\xab~\\xd9v\\xab"y\\x98\\x95\\xb5\\xd3\\\\\\xba'
#b'\\xed*V\\x9fk\\x97\\xd0\\x16\\xbdq\\xab~\\xd9v\\xab\"y\\x98\\x95\\xb5\\xd3\\\\\\xba'
