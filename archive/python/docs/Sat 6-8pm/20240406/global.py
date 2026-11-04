a = 1

def first():
    global a
    print(a)

def second():
    print(a)

def third(a):
    print(a)

def forth():
    a = 114
    print(a)

first()
second()
third(514)
forth() 