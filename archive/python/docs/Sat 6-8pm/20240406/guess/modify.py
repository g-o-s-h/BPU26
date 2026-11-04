import calculate as calc

### Modify

# 迭代所有内容
# 关卡号 + 1
# 生成一个随机答案（从 calculate 调用）
# 记录这个答案
# 开一个空的 list，用于后续记录用户的答案
def iterate() -> None:
    # level 关卡号
    # key 正确答案列表
    # answer 用户猜测列表
    global level, key, answer
    level += 1
    key.append(calc.get_random(level))
    answer.append([])

# 保存猜的结果
# 从参数里拿到一个数
# 把他存到 answer 的某个元素（list）里
def save_ans(user_guess: int) -> None:
    # answer 用户猜测列表
    global answer
    answer[-1].append(user_guess)


if __name__ == "__main__":
    level = 3
    key = [1, 2, 3]
    answer = [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
    ]
    iterate()
    print(level, key, answer)

    save_ans(114)
    print(answer)