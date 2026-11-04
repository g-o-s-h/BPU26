# 输入
text = input() + " "
count = 1

# 处理
for i in range(0, len(text) - 1):
    # i 和 i + 1
    if text[i] == text[i + 1]:
        count += 1
    else:
        print(text[i], end = "")
        if count > 1:
            print(count, end = "")
        count = 1