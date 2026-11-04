a, b = [int(each) for each in input().split()]
# result = a % b

# while result != 0:
#     a = b
#     b = result
#     result = a % b

while a % b != 0:
    a, b = b, a % b

print(b)