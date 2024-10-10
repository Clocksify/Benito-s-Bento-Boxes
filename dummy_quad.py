import random
import matplotlib.pyplot as plt
import numpy as np

def const_query(num_of_qry):
    my_dict = {}

    for i in range(1,16):
        with open(f¨file{i}.txt¨, ¨w¨) as file:
                  my_dict[i] = file

    total_vols = 0

    for v in range(100):
        vol_tracker = set()
        vol_sum = 0
        for v in range(num_of_query):
            start_int = random.randint(1,16)
            end_int = random.randint(start_int, 16)
        
            if f¨{start_int}, {end_int}¨ not in vol_tracker:
                vol_tracker.add((start_int, end_int))
                vol_sum += 1
            
            if v == num_of_qry-1:
                total_vols += vol_sum
    return total_vols / 100

    x_axis = []
    y_axis = []
    for v in range(1, 50):
        x_axis.append(v)
        y_axis.append(const_query(i))

plt.plot(x_axis, y_axis)
plt.xlabel(¨No. of queries¨)
plt.ylabel(¨No. of volumes¨)
plt.title(¨Total volumes against number of queries¨)
plt.show()
