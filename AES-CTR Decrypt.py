from Crypto.Cipher import AES

with open("my key.txt", "r") as secrets_file:
    key = secrets_file.readline().encode('utf-8')

    if len(key) < 32:
        key = key.ljust(32, b'\0')

    if len(key) > 32:
        key = key [:32]

with open("iv.txt", "rb") as iv_dest:
    iv = iv_dest.readline()

engine = AES.new(key, AES.MODE_CTR, nonce = iv)

with open("ciphertext.txt", "rb") as ciphertext_input:
    ciphertext = ciphertext_input.read()
    decrypted_ciphertext = engine.decrypt(ciphertext)

print(decrypted_ciphertext)

if (ValueError, KeyError):
    print("Incorrect decryption")

# Expected to print "Incorrect decryption" if nonce is any random value