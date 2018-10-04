BASE = 67108864 # 2**26
def random_n(n, base=BASE, mul=1103515245, bias=12345):
    remains = n
    f = 1
    while remains >= 1:
        f = (mul * f + bias) % base
        remains -= 1
    return f

def main(base=BASE, mul=1103515245, bias=12345, base2=2**10):
    next_gk = lambda gk_1: ((mul * gk_1 + bias) % base) % base2

    g0 = 1
    k, gk = 1, next_gk(1)

    while gk != g0:
        if k % 1000000 == 0:
            print(f'iter {k}: {gk}')
        k += 1
        gk = next_gk(gk) # 67108864
    
    print(k)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')