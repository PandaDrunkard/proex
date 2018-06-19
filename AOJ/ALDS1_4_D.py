def stdinput():
    from sys import stdin
    return stdin.readline().strip()

def main():
    n, k = map(int, stdinput().split())
    W = list(map(int, [stdinput() for _ in range(n)]))

    l, r = max(W), 100000*10000

    # 二分探索で上限値を確認する
    while l != r:
        mid = (l + r) // 2
        if calc_tracks(W, mid) <= k:
            r = mid
        else:
            l = mid + 1

    print(l)
        
def calc_tracks(W, P):
    ret = 0
    current_w = 0
    for w in W:
        if current_w + w > P:
            ret += 1
            current_w = w
        else:
            current_w += w
    return ret + 1

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')