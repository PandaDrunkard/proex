BASE = 67108864 # 2**26
def random_n(n, base=BASE, mul=1103515245, bias=12345):
    remains = n
    f = 1
    while remains >= 1:
        f = (mul * f + bias) % base
        remains -= 1
    return f

def main():
    for n in [2, 3]:
        result = random_n(n)
        print(result)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')