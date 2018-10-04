def main():
    m = 9
    n = 6

    a = zeros(m, n)
    b = zeros(n, m)

    c, reads = dot(a, b)

    print(reads)

def zeros(m, n):
    return [[0 for c in range(n)] for r in range(m)]

def dot(a, b):
    m = len(a)
    n = len(a[0])

    c = [[0 for c in range(m)] for r in range(m)]

    i = 0
    reads = 0
    while i < m:
        j = 0
        while j < m:
            d = 0
            k = 0
            while k < n:
                d = d + a[i][k] * b[k][j]
                reads += 2
                k += 1
            c[i][j] = d
            j += 1
        i += 1
    
    return c, reads

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')