def main():
    n = int(stdinput())
    S = [*map(int, stdinput().split())]
    q = int(stdinput())
    T = [*map(int, stdinput().split())]

    S = sorted(S)

    c = 0
    for t in T:
        if binary_search(S, len(S), t):
            c += 1
    
    print(c)

def binary_search(S, n, t):
    left = 0
    right = n - 1
    
    # print(*S)

    while left <= right:
        mid = (left + right) // 2

        # print(*[t, left, right, mid])
        # print(*[t, S[mid]])
        
        if S[mid] == t:
            return True
        elif S[mid] > t:
            right = mid - 1
        else:
            left = mid + 1
    
    return False

def stdinput():
    from sys import stdin
    return stdin.readline().strip()

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')