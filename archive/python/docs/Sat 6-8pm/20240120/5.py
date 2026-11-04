# 补全空格（补数）
n = int(input())

for i in range(n):
    # 通过分析第一行的空格数量，推算出“通项公式”
    for j in range(n - i - 1):
        print(" ", end = "")

    for j in range(i + 1):
        print("*", end = "")
    print()