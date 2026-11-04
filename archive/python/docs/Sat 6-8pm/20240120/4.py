# 题2 + 题3

n = int(input())

for i in range(n):
    # 内层循环的次数是变量，不再是固定的
    for j in range(i + 1):
        print("*", end = "")
    print()