import math

a, b, c = [int(each) for each in input().split()]
# 输出结果 a + b
p = 0.5 * (a + b + c)
result = math.sqrt(p * (p - a) * (p - b) * (p - c))
result = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(result)