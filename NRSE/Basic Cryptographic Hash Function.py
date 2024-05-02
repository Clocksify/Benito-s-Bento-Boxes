import hashlib

import hashlib
m = hashlib.sha256()
m.update(b"Nobody inspects")
digest = m.hexdigest()
print (m.digest())
print (digest)

with open("user input.txt", "r") as user_input:
    user_input = bytes(user_input.read() , 'utf-8')
    user_input = user_input.splitlines()

print (type(user_input))
m.update(user_input[0])
digest = m.hexdigest()
print (digest)


# encode it to bytes using UTF-8 encoding
# .hexdigest prints it in human readable form

