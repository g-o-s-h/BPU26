class File:
    def __init__(self, text: str):
        self.t = text
        self.pool = ""

    def dump(self, text: str):
        self.pool += text + "\n"

    def dump_self(self):
        self.dump(self.t)
    
    def clear_pool(self):
        print(self.pool)
        self.pool = ""

    def append(self, text: str):
        self.t += text
        return self
    
    def cut(self, pos: int, length: int):
        self.t = self.t[pos : pos + length]
        return self
        
    def insert(self, pos: int, text: str):
        self.t = self.t[:pos] + text + self.t[pos:]
        return self
    
    def find(self, substr: str):
        self.dump(str(self.t.find(substr)))
        return self

q = int(input())
file = File(input())

for turns in range(q):
    cmd = input().split()
    
    match int(cmd[0]):
        case 1:
            file.append(cmd[1]).dump_self()
        case 2:
            file.cut(int(cmd[1]), int(cmd[2])).dump_self()
        case 3:
            file.insert(int(cmd[1]), cmd[2]).dump_self()
        case 4:
            file.find(cmd[1])

file.clear_pool()