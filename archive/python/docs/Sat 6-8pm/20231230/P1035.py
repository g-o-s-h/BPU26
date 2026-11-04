# 输入
k = int(input())
s = 0 # sum 累加

# 处理
老王 = 0 # 迭代变量
while not s > k:
    老王 += 1 # 更新迭代变量
    s += 1 / 老王 # 求和

# 输出
print(老王)