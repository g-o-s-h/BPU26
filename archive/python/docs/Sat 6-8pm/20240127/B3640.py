text = input().split()

for i in range(len(text)):
    if text[i].isdigit(): # if only number
        text[i] = text[i][::-1] # reverse
    else: # other cases
        text[i] = text[i].swapcase() # swap case

for each in text[::-1]:
    print(each, end = " ")