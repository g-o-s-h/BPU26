from random import randint
from math import log

### Calc

# 根据难度计算机会次数
# 公式：log(关卡号 * 100, 2)
# 返回这个结果
def get_chance(level: int) -> int:
    return int(log(level * 100 - 1, 2)) + 1

# 判断数据合法化
# 拿到一个字符串
# 必须是数（阿拉伯数字 0 - 9 组成）
# 必须在范围内（第 level 关是 1 到 level * 100 之间）
# 合法返回 True，不合法返回 False
def is_valid(x: str, level: str) -> bool:
    if not x.isdigit():
        return False
    
    x = int(x)
    if x < 1 or x > level * 100:
        return False
    return True

# 根据关卡号，生成一个随机数
# 范围是 1 到 关卡号*100
def get_random(level: int) -> int:
    return randint(1, level * 100)


if __name__ == "__main__":
    for i in range(1, 11):
        print(get_chance(i)) # 7 8 9 9 9 10 10 10 10 10
    print(is_valid("114514", 10)) # False
    print(get_random(10)) # 一个 1 - 1000 之间的随机数