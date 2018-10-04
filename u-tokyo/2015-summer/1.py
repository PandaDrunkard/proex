import sys

def main():
    inp = sys.argv[1]

    result = to_i(inp)

    print(result)


def to_i(inp):
    base = 1
    ret = 0

    for c in reversed(str(inp)):
        n = int(c)
        ret += base * n
        base *= 4
    
    return ret

    
if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')