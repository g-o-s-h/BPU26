# init (initialization)
mod = "0123456789X"
a = list(input())
t = 0
j = 1

# process
for i in range(12):
    if a[i] == "-": # ingore "-"
        continue
    tmp = int(a[i]) # convert to int
    t += tmp * j    # sum all products
    j += 1          # iterate

s = t % 11          # mod 11

# output
if mod[s] == a[12]:
    print("Right")
else:
    a[12] = mod[s]
    print("".join(a))
    for k in a:
        print(k, end="")

# 废弃，将 10 转化为 X
# print("s=%d" % s)
# if s == 10:
#     x = "X"
# else:
#     x = str(s)