from Crypto.Hash import SHA256

with open("my key.txt", "r") as secrets_file:
    key = secrets_file.readline().strip().encode('utf-8')

    if len(key) < 32:
        hash_key = key.ljust(32, b'\0')

    if len(key) > 32:
        hash_key = key [:32]

s = int(input("What is your starting range? "))

e = int(input("What is your ending range? "))

Encrypted_query = []
print (type (Encrypted_query))

for j in range(s-1, e):
        hash = SHA256.new(data = bytes(str(j), 'utf-8'))
        Encrypted_query_item = hash.hexdigest()
        print (Encrypted_query_item)
        Encrypted_query.append(Encrypted_query_item + '\n')

print (Encrypted_query)
with open("NRSE/Encrypted_query.txt", "w") as Encrypted_query_dest:
        Encrypted_query_dest.writelines(Encrypted_query)
# with open("Benito-s-Bento-Boxes/NRSE/Encrypted_query.txt", "w") as EQ_to_EQR_dict_dest:
