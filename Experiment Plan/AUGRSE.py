
import math

result= []
levels = {}
levels[0]= {(1,node_end)}
for i in range(1, int(math.log(RSEmax, 2))+1):
    levels[i] = set()
    for node in levels[i-1]: #levels[0]: (1,8) levels[1]:{...} 
        mid = (node[0] + node[1]) // 2
        levels[i].add((node[0], mid))
        levels[i].add(((node[0]+mid)//2+1, (mid+1+node[1])//2))
        levels[i].add((mid+1, node[1]))

def cover(a, b):
    for i in range(1, int(math.log(RSEmax, 2))+1):
        for node in levels[i]:
            if (node[0] >= a) and (node[1] <= b):
                if 
    
    level_dict = dict(sorted(levels.items()))
    level_dict = {key: sorted(value) for key, value in level_dict.items()}
    
    for level, nodes in level_dict.items():
        for node in list(nodes):
            for n in result:
                condition = node[0] <= n[1] and node[0] <= n[1]
                if start <= node[0] and node[0] <= end and not condition:
                    result.append(node)
                    break
        continue
    
    return result

LOGmax = 8
print(cover_query(2, 6, 1, LOGmax))
