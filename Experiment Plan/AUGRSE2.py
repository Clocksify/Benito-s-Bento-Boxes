
import math

RSEmax = 8

result= []
levels = {}
levels[0]= {(1,RSEmax)}
for i in range(1, int(math.log(RSEmax, 2))+1):
    levels[i] = set()
    for node in levels[i-1]: #levels[0]: (1,8) levels[1]:{...} 
        mid = (node[0] + node[1]) // 2
        levels[i].add((node[0], mid))
        levels[i].add(((node[0]+mid)//2+1, (mid+1+node[1])//2))
        levels[i].add((mid+1, node[1]))

cover = []

def cover_query(a, b):
    for i in range(0, int(math.log(RSEmax, 2))+1):
        for node in levels[i]:
            if (node[0] >= a) and (node[1] <= b):
                for (start, end) in cover:
                    if not (node[0] > end or node[1] < start):
                        return False
                cover.append(node)
                return True

print(cover_query(2, 6))
