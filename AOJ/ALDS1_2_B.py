from sys import stdin
def stdinput():
    return stdin.readline().strip()

def main():
    n = int(stdinput())
    A = list(map(int, stdinput().split()))

    count = 0
    for i in range(n):
        min_idx = i
        for j in range(i, n):
            if A[j] < A[min_idx]:
                min_idx = j
        if min_idx != i:
            A[i], A[min_idx] = A[min_idx], A[i]
            count += 1
    
    print(' '.join(map(str, A)))
    print(count)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')