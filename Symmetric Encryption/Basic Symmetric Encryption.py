from cryptography.fernet import Fernet
import base64
# key can will be able to correctly decrypt ciphertext so long as the person encrypting the message also uses the same unchanged key
# use the same key each time, need to import the key from outside

#Import your key from outside of the script
# .strip() removes any leading or trailing whitespace from the string
# .encode() turns the string you read in the my key.txt into bytes

with open("my key.txt", "r") as secrets_file:
    key = secrets_file.readline().strip().encode('utf-8')

    if len(key) < 32:
        key = key.ljust(32, b'\0')

    if len(key) > 32:
        key = key [:32]

    base64encoded_key = base64.urlsafe_b64encode(key)
    print(base64encoded_key)


# Load your plaintext
with open("plaintext.txt", "r") as plaintext:
    plaintext = bytes(plaintext.read() , 'utf-8')
    plaintext_lines = plaintext.splitlines()
    

engine = Fernet(base64encoded_key)
# use this engine to encrypt and decrypt
# engine is of the Fernet class

#encrypting the plaintext
ciphertext = engine.encrypt(plaintext)
print (ciphertext)
with open("ciphertext.txt", "wb") as ciphertext_dest:
    ciphertext_dest.write(ciphertext)
# "wb" is write bytes

#decrypting the ciphertext
with open("ciphertext.txt", "rb") as ciphertext_input:
    ciphertext = ciphertext_input.read()
    decrypted_ciphertext = engine.decrypt(ciphertext)

with open("decrypted_ciphertext.txt", "r") as decrypted_ciphertext_dest:
     for line in decrypted_ciphertext_dest:
          decrypted_ciphertext = line.split()
          print(decrypted_ciphertext)

# good (?) bc it disguises frequency of characters and makes it harder to analyse the frequency 
# ciphertext is NOT the same length as plaintext
