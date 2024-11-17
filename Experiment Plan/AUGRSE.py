RSEmax = 8
import math

for i in range(1, math.log(8, 2)+1):
  level0 = ((1, RSEmax))
  for node in f"level{i-1}":
    f"level{i}" = set()
    mid = (node[0] + node[1]) // 2
    f"level{i}".add((node[0], mid))
    f"level{i}".add(((node[0]+mid)//2+1, (mid+1+node[1])//2))
    f"level{i}".add((mid, node[1]))
