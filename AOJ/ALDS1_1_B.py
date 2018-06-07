from sys import stdin
def stdinput():
    return stdin.readline().strip()

def main():
    a, b = map(int, stdinput().split())

    a, b = min(a, b), max(a, b)
    while b % a != 0:
        a, b = b % a, a
    
    print(a)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')