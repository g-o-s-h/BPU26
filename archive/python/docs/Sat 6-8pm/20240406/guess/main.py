import user_interface as ui
import calculate as calc
import modify

### Main

# 初始化
level = 0
answer = []
key = []

# 大循环
while True:
    
    ui.start_up()
    modify.iterate()

    for attempt in range(0, calc.get_chance(level)):
        user_guess = ui.guess()

        while calc.is_valid(user_guess):
            user_guess = ui.guess_again()
        
        modify.save_ans(user_guess)

        if user_guess == key[-1]:
            ui.aftermath(True) # win
            break
        else:
            ui.compare(user_guess, key[-1])
    
    else:
        ui.aftermath(False) # lose
    
    if not ui.checkpoint():
        break

ui.feedback()