def func(n):
    f1, f2 = 1, 1
    remains = n

    while remains > 2:
        f1, f2 = f1+f2, f1
        remains -= 1
    
    return f1

def to_i(s):
    n = 0
    for c in s:
        n = n *10 + int(c)
    return n

def to_s(n, scale=32):
    s = str(n)
    if len(s) < 32:
        s = '0' * (32 - (len(s))) + s
    return s

def main():
    f140 = func(140)

    print(to_s(f140)) # 81,055,900,096,023,504,197,206,408,605

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')