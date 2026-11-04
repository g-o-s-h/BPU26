# 题1 的升级版

n = int(input())
# n = int(input)
# for i in range(n)

# for i in range(n):
#     print("*" * n)

# 两层循环
for i in range(n):
    for j in range(n):
        print("*", end = "")
    print()