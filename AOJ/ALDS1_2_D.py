from sys import stdin
def stdinput():
    return stdin.readline().strip()

def main():
    n = int(stdinput())
    A = list(map(int, [stdinput() for _ in range(n)]))

    A, c, G = shell_sort(A, len(A))

    print(len(G))
    print(' '.join(map(str,G)))
    print(c)
    for a in A:
        print(a)

def insertion_sort(A, n, g):
    c = 0
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j = j - g
            c += 1
        A[j + g] = v
    return c

def shell_sort(A, n):
    G = sorted(iter_g(n), reverse=True)
    c = 0
    for g in G:
        c += insertion_sort(A, n, g)
    return A, c, G

def iter_g(n):
    v = 1
    d = 3
    while v <= n:
        yield v
        v += d
        d *= 3

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')