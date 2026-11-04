import users_interface as ui                    # 提示信息、用户交互（输入输出）、简单界面
import global_variable as val                   # 存储全局变量
import data_processing as calc                  # 计算，数据处理，判断合法性，生成随机数
import data_management as modify                # 修改数据，存储数据（增删改）
# import ui_sample as ui                        # 上一个模块的范例代码

### Main

while True:                                     # 大循环（死循环）
    
    modify.iterate()                            # 迭代变量
    ui.start_up()                               # 打印开局提示

    for attempt in range(calc.get_chance()):    # 循环（机会）
        user_guess = ui.guess(attempt)          # 让用户猜数

        while not calc.is_valid(user_guess):    # 当结果不合法时，进入循环
            user_guess = ui.guess_again()       # 重新要一个数
        
        user_guess = int(user_guess)            # 合法后转化为 int
        modify.save_ans(user_guess)             # 保存结果

        if user_guess == val.key[-1]:           # 如果猜对了
            ui.aftermath(True)                  # win
            break                               # 用 break 退出，不触发 for else
        else:                                   # 如果猜错了
            ui.compare(user_guess)              # 打印提示信息，继续猜
    
    else:                                       # 机会用完，自然退出，进入 for else
        ui.aftermath(False)                     # lose
    
    if not ui.checkpoint():                     # 如果用户不继续
        break                                   # 退出大循环

ui.feedback()                                   # 打印结算信息