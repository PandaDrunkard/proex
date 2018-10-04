BASE = 16777216 # 2**24
def random_n(n, base=BASE):
    remains = n
    f = 1
    while remains >= 1:
        f = (161 * f + 2457) % base
        remains -= 1
    return f

def main():
    n = 1000000
    result = random_n(n)

    print(result)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')