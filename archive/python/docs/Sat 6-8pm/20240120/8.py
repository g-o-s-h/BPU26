# 题7 + 题6
# 通过 题6 的方法，补上 题7 的下半部分
n = int(input())

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end = "")

    for j in range(i + 1):
        print("*", end = "")
    
    for j in range(i):
        print("*", end = "")
    print()

for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end = "")

    for j in range(i + 1):
        print("*", end = "")
    
    for j in range(i):
        print("*", end = "")
    print()
    