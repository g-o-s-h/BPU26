# Apple = map(int, input().split())
# Applelist = list(Apple)
# apple_list = list(map(int, input().split()))

apple_list = [int(each) for each in input().split()]
height = int(input()) + 30

# n = 0
count = 0
for i in range(10):
    if apple_list[i] <= height:
        # N=N+1
        count += 1

print(count)