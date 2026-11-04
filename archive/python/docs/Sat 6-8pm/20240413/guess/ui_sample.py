import global_variable as val                   # 存储全局变量
import data_processing as calc                  # 计算，数据处理，判断合法性，生成随机数

from os import system

### User Interface

# 开局提示信息
def start_up() -> None:
    system("cls")

    text = f"| 关卡: {val.level} | 机会: {calc.get_chance()} | 范围: 1 - {100 * val.level} |"
    barrier = "=" * (len(text) + 6)

    print('\n'.join([barrier, text, barrier]))

# 每次猜数的交互
def guess(attempt: int) -> str:
    return input(f"\n你还有 {calc.get_chance() - attempt} 次机会\n>>> ")

# 数据不合法的交互
def guess_again() -> str:
    return input("输入不合法，请重新输入。\n>>> ")

# 判断大小的交互
def compare(user_guess: int) -> None:
    if user_guess > val.key[-1]:
        print("太大了！")
    else:
        print("太小了！")

# 当局结算
def aftermath(is_win: bool) -> None:
	if is_win:
		print("恭喜你，答对了！")
	else:
		print("很抱歉，你的次数用光了。\n"
              "继续努力，你可以做得更好。")

# 是否继续
def checkpoint() -> bool:
    return input(
        "\n"
        "你是否希望继续？\n"
        "输入 \"EXIT\" 以退出，\n"
        "输入任何内容以继续。\n"
        ">>> "
    ).upper() != "EXIT"

# 汇总的游戏报告
def feedback() -> None:
    system("cls")

    for i in range(val.level):
        print(f"关卡 {i + 1} "
              f"{'胜利' if val.key[i] == val.answer[i][-1] else '失败'}\n"
              f"正确答案: {val.key[i]}\n"
              f"你的猜测: {val.answer[i]}\n")


# TEST
if __name__ == "__main__":
    val.level = 3
    start_up()

    val.key.append(calc.get_random())
    user_guess = guess(3)
    # print(user_guess, calc.is_valid(user_guess, level))

    while not calc.is_valid(user_guess):
        user_guess = guess_again()
        print(user_guess, calc.is_valid(user_guess))
    
    user_guess = int(user_guess)
    print(val.key[-1])
    compare(user_guess)

    aftermath(True)
    aftermath(False)

    print(checkpoint())
    
    system("pause")
    val.key = [111, 222, 333]
    val.answer = [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
    ]
    feedback()