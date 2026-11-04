q = int(input())
file = input().replace('\r', '')

for G2 in range(q):

    cmd = input().split()
    match cmd[0]:

        case '1':
            file += cmd[1]
            print(file)

        case '2':
            a, b = int(cmd[1]), int(cmd[2])
            file = file[a : a + b]
            print(file)

        case '3':
            a = int(cmd[1])
            file = file[:a] + cmd[2] + file[a:]
            print(file)

        case '4':
            print(file.find(cmd[1]))