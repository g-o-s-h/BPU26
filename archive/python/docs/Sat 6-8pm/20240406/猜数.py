from os import system
from random import randint

# 初始化
level = 1
chance = 7
answer = []
key = []

while True:

	# 界面
	system("cls")
	print(
"""--------------------------------------------------
| 关卡""", level, "| 机会:", chance, "| 范围 1 -", 100 * level, """|
--------------------------------------------------""")

	# 难度平衡
	if level % 4 == 0:
		chance += 1

	# 生成答案 & 记录
	key.append(randint(1, 100 * level))
	answer.append([])
	win = False

	for tries in range(0, chance):
		print("\n你还有", chance - tries, "次机会。")
		temp = input(">>> ")

		# legal restriction
		while not temp.isdigit() or int(temp) > 100 * level or int(temp) <= 0:
			print("输入不合法，请重新输入。")
			temp = input(">>> ")

		# save
		temp = int(temp)
		answer[level - 1].append(temp)

		if temp == key[-1]:
			win = True
			break
		elif temp > key[-1]:
			print("太大了！")
		else:
			print("太小了！")

	# check if win
	print()
	if win == True:
		print("恭喜你，答对了！")
	else:
		print("很抱歉，你的次数用光了。")
		print("继续努力，你可以做得更好。")
	
	# checkpoint
	check = input("""
你是否希望继续？
输入 \"EXIT\" 以退出，;
输入任何内容以继续。
>>> """)
	if check.upper() == 'EXIT':
		break

	# iteration
	level += 1

# feedback
system("cls")
for i in range(level):
	print("关卡", i)
	if key[i] == answer[i][-1]:
		print("胜利")
	else:
		print("失败")
	print("正确答案：", key[i])
	print("你的猜测：", answer[i])
	print()

system("pause")

