str1 = input()  # 输入的字符串
# 映射，表示字符 - 按键次数的关系
tab = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"," "]
c = 0           # count，统计最后按了几下
for i in str1:
    for j in tab:
        if i in j:
            c += j.index(i) + 1
print(c)