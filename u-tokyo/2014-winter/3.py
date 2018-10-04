def to_i(s):
    n = 0
    for c in s:
        n = n *10 + int(c)
    return n

def main():
    s1 = '00123456789012345678901234567890'
    s2 = '00987654321098765432109876543210'

    n1, n2 = to_i(s1), to_i(s2)

    n = n1 + n2

    print(n)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')