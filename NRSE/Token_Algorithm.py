from Crypto.Hash import SHA256

with open("Benito-s-Bento-Boxes/NRSE/my_key.txt", "r") as secrets_file:
    key = secrets_file.readline().strip().encode('utf-8')

    if len(key) < 32:
        hash_key = key.ljust(32, b'\0')

    if len(key) > 32:
        hash_key = key [:32]

Encrypted_query = []

start_int = input("What is your starting range? ")
end_int = input("What is your ending range? ")

for j in range(start_int, end_int+1):
        hash = SHA256.new(data = bytes(str(j), 'utf-8'))
        Encrypted_query_item = hash.hexdigest()
        Encrypted_query.append(Encrypted_query_item + '\n')

with open("Benito-s-Bento-Boxes/NRSE/Encrypted_query.txt", "w") as Encrypted_query_dest:
        Encrypted_query_dest.writelines(Encrypted_query)
# with open("Benito-s-Bento-Boxes/NRSE/Encrypted_query.txt", "w") as EQ_to_EQR_dict_dest:
