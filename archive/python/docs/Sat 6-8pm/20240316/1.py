a = int(input())
b = int(input())
print(a, "+", b, "=", a + b)

print("%d + %d = %d" % (a, b, a + b)) # 不看变量名

print("{a} + {b} = {result}".format(a = a, b = b, result = a + b)) # 不看变量类型
