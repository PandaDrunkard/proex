import sys

BASE = 16777216 # 2**24
def random_n(n, base=BASE):
    if n <= 0:
        return 1
    else:
        return (161 * random_n(n-1) + 2457) % base

def main():
    m = 100

    even = 0
    for n in range(m):
        result = random_n(n)
        if result % 2 == 0:
            even += 1

    print(even)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')