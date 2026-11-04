# 优化建议

# TODO: 切割 isbn code
def cut(isbn: str) -> tuple[str, str]:
    isbn_code = isbn.replace("-", "")  # 删除横线
    prefix = isbn_code[:-1] # 前九位
    suffix = isbn_code[-1]  # 校验码（最后一位）
    return prefix, suffix

# TODO: 计算校验码
def get_code(prefix: str) -> int:
    digits = [int(prefix[i]) * (i + 1) 
              for i in range(len(prefix))]  # 按公式把每一项乘出来
    return sum(digits) % 11  # 求和，模 11 并返回

convert = "0123456789X"

isbn = input()
prefix, suffix = cut(isbn)
my_suffix = convert[get_code(prefix)] # 自己算的校验码
if suffix == my_suffix:
    print("Right")
else:
    print(isbn[:-1] + my_suffix)


# "067082162"

# a = [int(each) for each in input().split()]

# ["10", "20", "44"]
# [10, 20, 44]