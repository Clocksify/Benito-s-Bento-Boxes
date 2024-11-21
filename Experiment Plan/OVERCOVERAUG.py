import math

RSEmax = 16

def is_power_of_two(x):
    return (x & (x - 1)) == 0

def overcoveraug(start, end):
    diff = (end - start) - 1
    while True:
        diff += 1
        if is_power_of_two(diff + 1):  # Check if diff + 1 is a power of 2
            N = math.log(diff + 1, 2)
            break
    if start == end:
        return (start, end)
    elif start == end - 1:
        return (start, end)
    else:
        for i in range(int(N), int(math.log(RSEmax, 2)) + 1):  # Ensure N is an integer
            for j in range(0, start):
                if (start - j) % 2**(i-1) == 1:
                    if start - j + 2**i - 1 >= end:
                        return (start - j, start - j + 2**i - 1)
                    else:
                        break
