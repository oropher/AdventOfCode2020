
from itertools import combinations 

with open('01/input','r') as f:
    data = [int(line.strip()) for line in f if int(line.strip()) < 2020]
    comb = combinations(data, 3)
    for i in list(comb):
        sum = 0
        for elem in i:
            sum += elem
        if sum == 2020:
            r = 1
            for elem in i:
                r *= elem
            print(r)