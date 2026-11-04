# init 
text = input() + " "
count = 1
# process & output
for i in range(len(text)-1):
    if text[i] == text[i+1]:
        count += 1
    else:
        print(text[i], sep = "", end = "")
        if count > 1:
            print(count, sep = "", end = "")
        count = 1