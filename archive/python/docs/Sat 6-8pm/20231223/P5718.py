## 输入

# 8
# 1 9 2 6 0 8 1 7
# 输入一个正整数 n
n = int(input())
# 输入 n 个非负整数
a = [int(each) for each in input().split()]

# 输入（字符串）
# a = input()
# 切割（按照空格切割）
# a = a.split()
# 推导式（根据 for each 处理）
# a = [int(each) for each in a]

## 处理
minimum = a[0]

for i in range(1, n):
    if a[i] < minimum:
        minimum = a[i]

## 输出
print(minimum)


## other choice
# print(min(a))