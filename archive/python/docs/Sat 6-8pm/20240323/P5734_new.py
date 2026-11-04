q = int(input())
file = input().replace('\r', '')

for turns in range(q):
    cmd = input().split()
    cmd[0] = int(cmd[0])

    if cmd[0] == 1:
        file += cmd[1]
        print(file)
    
    elif cmd[0] == 2:
        file = file[int(cmd[1]) : 
                    int(cmd[1]) + int(cmd[2])]
        print(file)
    
    elif cmd[0] == 3:
        file = file[:int(cmd[1])] + cmd[2] + file[int(cmd[1]):]
        print(file)

    elif cmd[0] == 4:
        print(file.find(cmd[1]))