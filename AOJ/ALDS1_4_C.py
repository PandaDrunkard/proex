def main():
    n = int(stdinput())

    st = [None] * (4**12)

    for _ in range(n):
        cmd, value = stdinput().split()
        if cmd == 'insert':
            st[get_hash(value)] = 1
        elif cmd == 'find':
            if st[get_hash(value)] == 1:
                print('yes')
            else:
                print('no')

CODES = {'A' : 1, 'C' : 2, 'G' : 3, 'T' : 4}
def get_hash(s):
    base = 1
    h = 0
    for c in s:
        code = CODES[c]
        h += code * base
        base *= 4
    return h

def stdinput():
    from sys import stdin
    return stdin.readline().strip()

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')