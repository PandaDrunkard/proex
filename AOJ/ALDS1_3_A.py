from sys import stdin
def stdinput():
    return stdin.readline().strip()

def main():
    A = list(map(convert, stdinput().split()))
    frame = []
    while len(A) > 0:
        frame.append(A.pop())
        while can_calc(frame):
            v1 = frame.pop()
            v2 = frame.pop()
            op = frame.pop()
            if op == '+':
                frame.append(v1 + v2)
            elif op == '-':
                frame.append(v1 - v2)
            elif op == '*':
                frame.append(v1 * v2)
    print(*frame)

OPERANTS = ('+', '-', '*')
def convert(a):
    if a in OPERANTS:
        return a
    else:
        return int(a)

def can_calc(s):
    if len(s) < 3:
        return False
    else:
        return s[-3] in OPERANTS and type(s[-2]) is int and type(s[-1]) is int

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')