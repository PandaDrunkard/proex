from sys import stdin
def stdinput():
    return stdin.readline().strip()

def main():
    n = int(stdinput())
    inputs = list(map(int, [stdinput() for _ in range(n)]))

    primes = 0
    for a in inputs:
        if is_prime(a, None):
            primes += 1
    print(primes)

def is_prime(a, primes):
    # Search for num below a**0.5,
    # as when A can be devided by number > a**0.5,
    # it means existing number < a**0.5 also can devide A.
    for p in range(2, int(a ** 0.5)  + 1):
        if a % p == 0:
            return False
    return True

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')