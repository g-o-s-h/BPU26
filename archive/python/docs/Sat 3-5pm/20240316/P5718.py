n = int(input())
numbers = [int(each) for each in input().split()]
minimum = numbers[0]

for i in range(1, n):
    if numbers[i] < minimum:
        minimum = numbers[i]

print(minimum)