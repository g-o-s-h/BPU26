# 题4 的升级版
n = int(input())

for i in range(n):
    for j in range(i + 1):
        print("*", end = "")
    print()

# 意识到 range 可以倒着用
for i in range(n - 2, -1, -1):
    for j in range(i + 1):
        print("*", end = "")
    print()