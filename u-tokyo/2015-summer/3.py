import sys

def main():
    inp = sys.argv[1]

    result = to_hex(inp)
    result = to_a(result)

    print(result)

def to_num(alphabets, offset=ord('a')):
    ret = ''
    for a in alphabets:
        ret += str(ord(a) - offset)
    
    return ret

def to_a(nums, offset=ord('a')):
    ret = ''
    for n in str(nums):
        ret += chr(int(n) + offset)
    return ret

def to_i(inp, mod=8):
    base = 1
    ret = 0

    for c in reversed(str(inp)):
        n = int(c)
        ret += base * n
        base *= mod
    
    return ret

def to_hex(inp, mod=8):
    value = int(inp)
    ret = []
    while value != 0:
        ret.append(value % mod)
        value = value // mod

    return ''.join(map(str,reversed(ret)))
    
if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')