from Crypto.Hash import KMAC256

with open("my key.txt", "r") as secrets_file:
    hash_key = secrets_file.readline().strip().encode('utf-8')

    if len(hash_key) < 32:
        hash_key = hash_key.ljust(32, b'0')

    if len(hash_key) > 32:
        hash_key = hash_key [:32]

print (hash_key)
# Expected output is Password123 with 0s added at the end until the object is 32 bytes long
# KMAC256 provides a security strength of 256 bits. Key is 32 bytes or more

mac = KMAC256.new(key=hash_key, mac_len=8)

with open("plaintext.txt", "r") as plaintext:
    for line in plaintext:
        line = line.strip().encode('utf-8')
        mac.update(line)
        

print(mac.hexdigest())
# Expected output is digest that is 16 characters long
