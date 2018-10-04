import sys

def main():
    inp = sys.argv[1]

    result = to_num(inp)
    result = to_i(result)

    print(result)

def to_num(alphabets, offset=ord('a')):
    ret = ''
    for a in alphabets:
        ret += str(ord(a) - offset)
    
    return ret


def to_i(inp, mod=8):
    base = 1
    ret = 0

    for c in reversed(str(inp)):
        n = int(c)
        ret += base * n
        base *= mod
    
    return ret

    
if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')