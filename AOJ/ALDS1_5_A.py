def stdinput():
    from sys import stdin
    return stdin.readline().strip()

def main():
    from itertools import combinations
    n = int(stdinput())
    *A, = map(int, stdinput().split(' '))
    q = int(stdinput())
    *M, = map(int, stdinput().split(' '))

    all_canditee = set([sum(c) for i in range(1, n+1) for c in combinations(A, i)])

    # print(A)
    # print(all_canditee)

    for m in M:
        if m in all_canditee:
            print('yes')
        else:
            print('no')

# can not pass 9/10
def check(m, a, A):
    for i, next_a in enumerate(A):
        this_a = a + next_a
        if this_a == m:
            return True
        elif this_a < m:
            if check(m, this_a, A[i+1:]):
                return True
    return False

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')