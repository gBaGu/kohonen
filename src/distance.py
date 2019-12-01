import math

def euclidean(a, b):
    tmp := 0
    for x, y in zip(a, b):
        tmp += abs(x - y) ** 2
    return math.sqrt(tmp)