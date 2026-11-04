def generate(mode: str, a: int, b: int):
    match mode:
        case "a":
            result = "{a}+{b}={c}".format(a = a, b = b, c = a + b)
        case "b":
            result = "{a}-{b}={c}".format(a = a, b = b, c = a - b)
        case "c":
            result = "{a}*{b}={c}".format(a = a, b = b, c = a * b)
    print(result, len(result), sep = "\n")

n = int(input())
mode = "a"

for turns in range(n):
    cmd = input().split()
    if len(cmd) == 3:
        mode = cmd[0]
        a, b = int(cmd[1]), int(cmd[2])
    else:
        a, b = int(cmd[0]), int(cmd[1])
    generate(mode, a, b)