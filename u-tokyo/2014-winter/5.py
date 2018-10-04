def to_f(s):
    base, exp = s.split(' ')
    
    f = []
    for c in reversed(base):
        f.append(int(c))
    
    return f, int(exp)

def mul_f(f1, f2):
    b1, e1 = f1
    b2, e2 = f2
    size = len(b1)

    ret = [0 for _ in range(2 * size)]
    for i1, d1 in enumerate(b1):
        s = 0 # 繰り上がり
        for i2, d2 in enumerate(b2):
            tmp = ret[i1 + i2] + d1 * d2 + s
            s = tmp // 10
            ret[i1 + i2] = tmp % 10
        ret[i1 + len(b2)] += s
    
    exp = 0
    if ret[-1] == 0:
        ret = ret[:-1]
        exp = -1
    
    base, exp = ret[-size:], e1 + e2 + 1 + exp

    return base, exp

def to_s(f):
    base, exp = f
    s_base = ''
    for i in reversed(base):
        s_base += str(i)
    
    s_exp = str(exp)
    if len(s_exp) < 2:
        s_exp = '0' + s_exp
    
    return s_base + ' ' + s_exp

def main():
    s1 = '12345678901234567890123456789012 04'
    s2 = '98765432109876543210987654321098 09'

    f1 = to_f(s1)
    f2 = to_f(s2)

    f3 = mul_f(f1, f2)

    print(to_s(f3))

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')