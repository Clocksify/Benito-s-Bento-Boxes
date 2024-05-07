from Crypto.Cipher import AES 

with open("Benito-s-Bento-Boxes/my key.txt", "r") as secrets_file:
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
   for line in j:
      ciphertextline = line.rstrip()
      print(ciphertextline)

      
  #      Answer = d_cipher.decrypt(bytes(ciphertextline,'utf-8'))
   #     open("Benito-s-Bento-Boxes/NRSE/Answer.txt",'a').write(str(Answer))


