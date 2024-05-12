from Crypto.Cipher import AES 

with open("Benito-s-Bento-Boxes/NRSE/my_key.txt", "r") as secrets_file:
    key = secrets_file.readline().strip().encode('utf-8')

    if len(key) < 32:
        hash_key = key.ljust(32, b'\0')

    if len(key) > 32:
        hash_key = key [:32]

with open('Benito-s-Bento-Boxes/NRSE/iv.txt','rb') as f:
    iv = f.readline()
    print(iv)

d_cipher = AES.new(hash_key, AES.MODE_CTR, nonce = iv)

open("Benito-s-Bento-Boxes/NRSE/Answer.txt",'w').close()

with open("Benito-s-Bento-Boxes/NRSE/Response.txt") as j:
  with open("Benito-s-Bento-Boxes/NRSE/Answer.txt",'w') as g:
    for line in j:
      ciphertextline = line.rstrip()
      Stripped = (ciphertextline[2:-1])
      print(bytes(Stripped, 'utf-8'))
      Cream = bytes(Stripped,'utf-8')
      Creamer = Cream.decode('unicode-escape').encode('ISO-8859-1')
      Answer = d_cipher.decrypt(Creamer)
      print(Answer)
      g.write(str(Answer)+'\n')
#b'\xed*V\x9fk\x97\xd0\x16\xbdq\xab~\xd9v\xab"y\x98\x95\xb5\xd3\\\xba'
#b'\\xed*V\\x9fk\\x97\\xd0\\x16\\xbdq\\xab~\\xd9v\\xab"y\\x98\\x95\\xb5\\xd3\\\\\\xba'
#b'\\xed*V\\x9fk\\x97\\xd0\\x16\\xbdq\\xab~\\xd9v\\xab\"y\\x98\\x95\\xb5\\xd3\\\\\\xba'
