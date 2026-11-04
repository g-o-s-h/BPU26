text = input()
l = len(text)
result = text[0]

count = 1
for i in range(1, l):
    if text[i] == text[i - 1]:
        count += 1
    
    else:
        if count > 1:
            result += str(count)
        result += text[i]
        count = 1

if count > 1:
    result += str(count)

print(result)