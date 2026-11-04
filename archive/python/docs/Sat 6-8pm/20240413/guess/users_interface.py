import global_variable as val                   # 存储全局变量
import data_processing as calc                  # 计算，数据处理，判断合法性，生成随机数

from os import system

### User Interface

# Allen          
# 开局提示信息
# 从 value 拿到 level
# 分析出关卡、机会、范围，整理格式输出
def start_up() -> None:
    system("cls")

    text = f"| 关卡: {val.level} | 机会: {calc.get_chance()} | 范围: 1 - {100 * val.level} |"
    barrier = "=" * (len(text) + 6)

    print('\n'.join([barrier, text, barrier]))
        

# Daniel
# 每次猜数的交互
# 从参数列表拿到当前猜测的次数
# 用 calc 计算剩余机会
# 整理格式输出的同时，
# 问用户要一个输入的数，并把这个数 return
# （因为还不确定这个“数”是否合法，所以先存成字符串以便检查）
def guess(attempt: int) -> str:
    return input(f"\n你还有 {calc.get_chance() - attempt} 次机会\n")
    
# Daniel
# 数据不合法的交互
# 再问用户要一个输入
def guess_again() -> str:
    return input("输入的数不合法，重新输入\n")


# Allen
# 判断大小的交互
# 从参数列表拿用户的猜测
# 从 value 拿答案
# 比较并输出提示信息（大了、小了之类的）
def compare(user_guess: int) -> None:
    if user_guess > val.key[-1]:
        print("太大了")
    else:
        print("太小了")
            

# Daniel
# 当局结算
# 从参数列表拿输赢（一个 bool）
# 根据输赢给出庆祝、鼓励的话
def aftermath(win: bool) -> None:
    if win:
        print("你真棒，答对了")
    else:
        print("很抱歉，你输了，继续加油")
        
        
# Allen
# 是否继续
# 输出提示信息，询问用户是否继续
# 推荐问用户要输入，按结果判断是否继续
def checkpoint() -> bool:
    return input(
        "\n"
        "你是否继续？\n"
        "输入\"EXIT\"可以退出，\n"
        "输入任何以继续\n"
        ">>> "
    ).upper() !="EXIT"


# Daniel
# 汇总的游戏报告
# 从 value 拿所有 key 和 answer
# 梳理格式，并全部输出
def feedback() -> None:
    system("cls")

    for i in range(val.level):
        if val.key[i] == val.answer[i][-1]:
            is_win = "胜利"
        else:
            is_win = "失败"
        print(f"关卡 {i + 1} {is_win}")
        print(f"正确答案：{val.key[i]}")
        print(f"你的猜测：{val.answer[i]}\n")

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