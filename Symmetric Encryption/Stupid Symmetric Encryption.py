def xor_encrypt(data, key):
    # encrypts data with XOR operation using key
    encrypted_data = bytearray()
    for i in range(len(data)):
        encrypted_data.append(data[i] ^ key[0])
    return bytes(encrypted_data)

# for every character in the length of the data input, that character is XORed by the 1st byte of the key
# hence the key basically becomes 1 bytes
# XOR is done by ^

def xor_decrypt(encrypted_data, key):
    return xor_encrypt(encrypted_data, key)

key = b"4"  
data = b"apples beetroots carrots donkeys elephants fairies"
# \x00 represents a byte with value of 0 in hexadecimal

encrypted_data = xor_encrypt(data, key)
print(encrypted_data)

decrypted_data = xor_decrypt(encrypted_data, key)
print(decrypted_data)

# bad because the same byte gets applied to each character of the plaintext individually
# does not disguise frequency of letters
# ciphertext is same length as plaintext
# boooo that's bad
