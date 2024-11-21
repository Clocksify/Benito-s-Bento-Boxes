import math 
RSEmax = 16
b = 0
query_list = []
def cover_log(start_int, end_int):
    while start_int <= end_int:
        b = start_int
        for i in range(2, int(math.log(RSEmax, 2))+1):
            if end_int == start_int + 1:
                b = end_int
                break
            if start_int % 2 == 0:
                if end_int - start_int < 4:
                    b = start_int + 1
                    break
                else:
                    b = start_int
                    break
            if start_int + (2**i -1) > end_int:
                break
            else:    
                b = start_int + (2**i -1)
            if start_int % 2**(i-1) != 1:
                b = start_int + (2**(i-1) -1)
                break   
      
        node = (start_int, b)
        query_list.append(node)
        start_int = b+1
    return query_list
