import math

n = int(input())

if n <= 1:
    print(f"{n} 不是质数")

for i in range(2, math.sqrt(n)):
    if n % i == 0:
        print(f"{n} 不是质数")
        break
else:
    print(f"{n} 是质数")
