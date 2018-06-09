from sys import stdin
def stdinput():
    return stdin.readline().strip()

def main():
    n = int(stdinput())
    A = list(map(int, stdinput().split()))

    done = True
    count = 0
    while done:
        done = False
        for i in range(n-1, 0, -1):
            if A[i] < A[i-1]:
                A[i], A[i-1] = A[i-1], A[i]
                done = True
                count += 1
    
    print(' '.join(map(str, A)))
    print(count)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')