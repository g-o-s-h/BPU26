n = int(input())

if n == 1 or n == 2:
    print(1)
    
else:
    a = 1
    b = 1

    for i in range(2, n):
        result = a + b
        # 迭代 / 更新
        a = b
        b = result

    print(result)