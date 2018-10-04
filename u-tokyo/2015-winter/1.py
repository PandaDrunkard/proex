import sys

BASE = 16777216 # 2**24
def random_n(n, base=BASE):
    if n <= 0:
        return 1
    else:
        return (161 * random_n(n-1) + 2457) % base

def main():
    n = int(sys.argv[1])
    result = random_n(n)

    print(result)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')