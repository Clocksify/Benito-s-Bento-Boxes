H = []
EDS = {}

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
  with open(f"Benito-s-Bento-Boxes/file{i}.txt", "r") as file:
        file = file.readline().strip().encode('utf-8')
        e_cipher = AES.new(hash_key, AES.MODE_CBC)
        f"ciphertext{i}" = e_cipher.encrypt(pad(file, AES.block_size))
  
for node in H:
  hash = SHA256.new(data = bytes(str(node), 'utf-8'))
  hash_node = hash.hexdigest()
  for v in range(node[0], node[1]):
    EDS[hash_node] = f"ciphertext{i}"
  
  
     
