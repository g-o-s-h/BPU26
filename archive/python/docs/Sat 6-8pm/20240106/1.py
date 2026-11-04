# 输入
n = int(input())

# 处理
# 前提条件
fib = [1, 1]
for i in range(2, n):
    # 通项公式（任何时候都通用）
    fib.append(fib[i - 1] + fib[i - 2])

print(fib[n - 1])