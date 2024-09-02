H = []
EDS = {}

for i in range(1, 4):
    hash = SHA256.new(data = bytes(str(i), 'utf-8'))
    hash_attr = hash.hexdigest()
    with open(f"Benito-s-Bento-Boxes/NRSE/file{i}.txt", "r") as name:
        name = name.readline().strip().encode('utf-8')
        e_cipher = AES.new(hash_key, AES.MODE_CBC)
        ciphertext = e_cipher.encrypt(pad(name, AES.block_size))
        iv = e_cipher.iv
        iv_dict[i] = iv
        EQ_to_EQR_dict[hash_attr] = [ciphertext]

def node(start, end):
  if start = end:
    H += (start, start)
  mid = (start + end) // 2
  left_child = node(start, mid)
  right_child = node(mid+1, end)
  H += left_child
  H += right_child

node(1, LOG.max)

for i in range(1, LOG.max):
  with open(f"Benito-s-Bento-Boxes/NRSE/file{i}.txt", "r") as file:
        file = file.readline().strip().encode('utf-8')
        e_cipher = AES.new(hash_key, AES.MODE_CBC)
        f"ciphertext{i}" = e_cipher.encrypt(pad(file, AES.block_size))
  
for node in H:
  hash = SHA256.new(data = bytes(str(node), 'utf-8'))
  hash_attr = hash.hexdigest()
  for v in range(node[0], node[1]):
    EDS[node] = f"ciphertext{i}"
  
  
     
