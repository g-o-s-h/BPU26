import math

prime_table = []

n = int(input())

for i in range(2, n + 1):
    for each in prime_table:
        if i % each == 0:
            break
    else:
        prime_table.append(i)

print(prime_table)