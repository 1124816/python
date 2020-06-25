def func(infunc):
    def returner(*f):
        return infunc(*f) 
    return returner

def other(*f):
    for i in f:
        print(i)

print(func(other)('bob', 'tim'))
