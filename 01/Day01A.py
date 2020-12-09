
from itertools import combinations 

with open('01/input','r') as f:
    data = [int(line.strip()) for line in f if int(line.strip()) < 2020]
    comb = combinations(data, 2)
    for i in list(comb):  
        if (i[0]+i[1]) == 2020:
            print(i[0]*i[1])