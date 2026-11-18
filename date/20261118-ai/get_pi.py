from random import random
from math import sqrt
from time import perf_counter

DARTS = 12 * (10 ** 7)
hits = 0
perf_counter()

for i in range(1, DARTS):
    x, y = random(), random()
    dist = sqrt(x ** 2 + y ** 2)
    
    if dist <= 1.0:
        hits += 1

pi = 4 * (hits / DARTS)

print(f"pi 的值：{pi}\n运行时间：{perf_counter()}")