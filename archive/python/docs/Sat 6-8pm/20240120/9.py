# 题8 的升级版
# 学会控制 i 和 j 的走向，到底是增加 or 减少，到底从谁开始到谁结束
n = int(input())

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end = "")

    for j in range(i + 1):
        print(j + 1, end = "")
    
    for j in range(i - 1, -1, -1):
        print(j + 1, end = "")
    print()

for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end = "")

    for j in range(i + 1):
        print(j + 1, end = "")
    
    for j in range(i - 1, -1, -1):
        print(j + 1, end = "")
    print()
    