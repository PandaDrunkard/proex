def main():
    n = int(stdinput())
    S = [*map(int, stdinput().split())]
    q = int(stdinput())
    T = [*map(int, stdinput().split())]

    S = sorted(S)
    T = sorted(T)

    i = j = c = 0

    while i < n and j < q:
        if S[i] == T[j]:
            c += 1
            i += 1
            j += 1
        elif S[i] > T[j]:
            j += 1
        else:
            i += 1
    
    print(c)

def stdinput():
    from sys import stdin
    return stdin.readline().strip()

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')