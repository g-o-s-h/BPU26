import global_variable as val                   # 存储全局变量
import data_processing as calc                  # 计算，数据处理，判断合法性，生成随机数

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
    val.level += 1
    val.key.append(calc.get_random())
    val.answer.append([])

# 保存猜的结果
# 从参数里拿到一个数
# 把他存到 answer 的某个元素（list）里
def save_ans(user_guess: int) -> None:
    # answer 用户猜测列表
    val.answer[-1].append(user_guess)


# TEST
if __name__ == "__main__":
    val.level = 3
    val.key = [1, 2, 3]
    val.answer = [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
    ]
    iterate()
    print(val.level, val.key, val.answer)

    save_ans(114)
    print(val.answer)