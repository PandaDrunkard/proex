from sys import stdin
def stdinput():
    return stdin.readline().strip()

from collections import deque

def main():
    n ,q = map(int, stdinput().split())
    ps = deque()
    for _ in range(n):
        p, t = stdinput().split()
        t = int(t)
        ps.append([p, t])

    ctime = 0
    while len(ps) > 0:
        p = ps.popleft()
        if p[1] <= q:
            ctime += p[1]
            print(f'{p[0]} {ctime}')
        else:
            ctime += q
            p[1] -= q
            ps.append(p)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')