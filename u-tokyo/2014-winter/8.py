class Float32():

    @staticmethod
    def from_s(s):
        s_base, s_exp = s.split(' ')
        base = []
        for c in reversed(s_base):
            base.append(int(c))
        return Float32(base, int(s_exp))

    @staticmethod
    def from_i(i):
        exp = len(str(i)) - 1
        base = []
        for c in reversed(str(i)):
            base.append(int(c))
        return Float32(base, exp)

    SIZE = 32
    def __init__(self, base, exp):
        self.base = base
        self.exp = exp

        # 120 => 12000000000000000000000000000000
        if len(self.base) < Float32.SIZE:
            self.base = [0] * (Float32.SIZE - len(self.base)) + self.base

    def __add__(self, f2):
        base1, exp1 = self.base, self.exp
        base2, exp2 = f2.base, f2.exp

        size = len(base1)
        max_size = size + max(exp1, exp2)

        base = [0 for _ in range(max_size + 1)]
        base1 = ([0] * exp1) + base1 + ([0] * (max_size - size - exp1))
        base2 = ([0] * exp2) + base2 + ([0] * (max_size - size - exp2))

        s = 0
        for i, (d1, d2) in enumerate(zip(base1, base2)):
            tmp = d1 + d2 + s
            s = tmp // 10
            c = tmp % 10
            base[i] = c
        base[-1] = s

        exp = max(exp1, exp2) + 1
        while base[-1] == 0:
            base = base[:-1]
            exp -= 1
        
        return Float32(base[-size:], exp)

    def __sub__(self, f2):
        base1, exp1 = self.base, self.exp
        base2, exp2 = f2.base, f2.exp

        size = len(base1)
        max_size = size + max(exp1, exp2)

        base = [0 for _ in range(max_size + 1)]
        base1 = ([0] * exp1) + base1 + ([0] * (max_size - size - exp1))
        base2 = ([0] * exp2) + base2 + ([0] * (max_size - size - exp2))

        s = 0
        for i, (d1, d2) in enumerate(zip(base1, base2)):
            tmp = d1 - d2 + s
            if tmp < 0:
                s = -1
                c = tmp + 10
            else:
                s = 0
                c = tmp
            base[i] = c
        if s < 0:
            raise Exception()

        exp = max(exp1, exp2) + 1
        while base[-1] == 0 and exp>0:
            base = base[:-1]
            exp -= 1
        
        return Float32(base[-size:], exp)

    def __mul__(self, f2):
        b1, e1 = self.base, self.exp
        b2, e2 = f2.base, f2.exp
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
        return Float32(base, exp)

    def div_i(self, n):
        base1, exp1 = self.base, self.exp
        base1 = [0] + base1

        base = [0 for _ in range(Float32.SIZE + 1)]
        exp = exp1

        s = 0
        for i, d1 in enumerate(reversed(base1)):
            d = s * 10 + d1
            s = d % n
            c = d // n
            base[i] = c
        base[-1] = (s * 10) // n

        base = list(reversed(base))

        if base[-1] == 0:
            base = base[:-1]
            exp -= 1

        return Float32(base[-Float32.SIZE:], exp)

    def __pow__(self, n):
        remains = n
        
        ret = Float32.from_s('1 0')

        while remains > 0:
            ret = self.__mul__(ret)
            remains -= 1
        
        return ret

    def __gt__(self, f2):
        base1, exp1 = self.base, self.exp
        base2, exp2 = f2.base, f2.exp

        size = len(base1)
        max_size = size + max(exp1, exp2)

        base = [0 for _ in range(max_size + 1)]
        base1 = ([0] * exp1) + base1 + ([0] * (max_size - size - exp1))
        base2 = ([0] * exp2) + base2 + ([0] * (max_size - size - exp2))

        for d1, d2 in zip(reversed(base1), reversed(base2)):
            if d1 == 0 and d2 == 0:
                continue
            else:
                return d1 > d2
        
        return False

    def __str__(self):
        base, exp = self.base, self.exp
        s_base = ''
        for i in reversed(base):
            s_base += str(i)
        
        s_exp = str(exp)
        if len(s_exp) < 2:
            s_exp = '0' + s_exp
        
        return s_base + ' ' + s_exp

def f_x(x):
    f1, f2 = 1, 1
    remains = x

    while remains > 2:
        f1, f2 = f1+f2, f1
        remains -= 1
    
    return Float32.from_i(f1)

def g_x(x):
    two = Float32.from_s('2 00')
    one = Float32.from_s('1 00')
    phi = Float32.from_s('17247448713915890490986420373529 00')
    root_five = phi * two - one

    phi_x = (phi ** x)

    phi_lower = Float32.from_s('100 00')
    phi_upper = Float32.from_s('100 33')

    for _ in range(200):
        v_lower = phi_lower * root_five
        v_upper = phi_upper * root_five
        v_mean = (v_lower + v_upper).div_i(2)
        if v_mean > phi_x:
            phi_upper = (phi_upper + phi_lower).div_i(2)
        else:
            phi_lower = (phi_upper + phi_lower).div_i(2)
    
    return (phi_lower + phi_upper).div_i(2)

def main():
    max_diff, max_x = Float32.from_i(1), -1
    for x in range(1, 141):
        f, g = f_x(x), g_x(x)
        d = g - f
        if d > max_diff:
            max_diff = d
            max_x = x
        
        print(f'x:{max_x}, diff:{max_diff}')
    
    print(x)


if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')