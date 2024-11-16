def node(start, end):
    global EDS
    if start == end:
        if (start, start) not in EDS:  
            EDS.append((start, start))
        return (start, start)
    
    mid = (start + end) // 2
    left_child = node(start, mid)
    right_child = node(mid + 1, end)
    
    if left_child not in EDS:
        EDS.append(left_child)
    
    if right_child not in EDS:
        EDS.append(right_child)
    
    combined = (left_child[0], right_child[1])
    if combined not in EDS:
        EDS.append(combined)
    
    return combined

def over_cover(a, b, LOGmax):
  nodes_in_range = []
  min_node = []
  minimum_range = LOGmax
  for node in EDS:
    if node[0] <= a and node[1] >= b:
      nodes_in_range.append(node)
  for node in nodes_in_range:
    if node[1] - node[0] < minimum range:
      minimum_range = node[1] - node[0]
      min_node.clear()
      min_node.append(node)
  return min_node
    
