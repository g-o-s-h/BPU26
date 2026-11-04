range(10) # end
# 0 1 2 3 4 5 6 7 8 9
range(1, 10) # start, end
# 1 2 3 4 5 6 7 8 9
range(1, 10, 3) # start, end, step
# 1 4 7

# 变量类型
int
float
bool
str
list

# 定义
list1 = [1, 2, 3]
list2 = [1, 3.14, 114.514]
list3 = [1, 3.14, True, "abcabc鸡你太美"]
list4 = [list1, list2, list3, [1, 2, [3, 4, 5]]]

# 加法（链接）
# "abc" + "123" -> "abc123"
list1 + list2

list1[2] = 100

list4[1] = 10

list1 += [123]
list1.append(123)
# ['a', 'b', 'c', 'd', 'e']
del list1[3]
# ['a', 'b', 'c', 'e']
del list1[3]
# ['a', 'b', 'c']

