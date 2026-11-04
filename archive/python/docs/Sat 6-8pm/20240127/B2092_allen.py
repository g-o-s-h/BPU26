# True 开
# False 关

# 输入
n = int(input())
# a = input().split()
# st = int(a[0])

# 声明
light = [True] * (n + 1)
# list = []

# 处理
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j % i == 0:
            light[j] = not light[j]

# 输出
for i in range(1, n + 1):
    if not light[i]:
        print(i, end = " ")

# for i in range(ac):
#     if (i == 1)%2 == 0:
#         light .apper(ture)
#     else:
#     for j in range (3,st=1):
#     for k in range(ac):
#     if (k=1)%j == 0:
# if light [k] == ture:
#     light [k] == false
#         else:
# light [k] == ture 
# for i in range(st):
#     if light i == false
#     ist.append(i=1)
# for i in range(len(list)):
#     if i == 0
#     print (list [i],end=" ")
#     else:
#         print(",",end = " ")
#         print(list [i],end" ")