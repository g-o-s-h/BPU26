text = input().split()[::-1]

for i in range(len(text)):
    
    if text[i].isalpha():
        text[i] = text[i].swapcase()
    
    if text[i].isdigit():
        text[i] = text[i][::-1]

for each in text:
    print(each, end = " ")


# text = input().split()

# for i in range(len(text)):
#     if text[i].isdigit(): # if only number
#         text[i] = text[i][::-1] # reverse
#     else:
#         text[i] = text[i].swapcase()

# for each in text[::-1]:
#     print(each, end = " ")