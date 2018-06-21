def main():
    A = [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]
    ]
    B = [
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4]
    ]

    C, reads = dot(A, B, 4, 3)

    print(C)
    print(reads)

    m = read_matrix()
    print(len(m))
    print(len(m[0]))

    m1 = read_matrix()
    m2 = read_matrix('mat2.txt')

    m3 = dot(m1, m2, len(m1), len(m1[0]))[0]
    print(m3)
    print(trace(m3))

    C, reads = cached_dot(A, B, 4, 3, 8)
    print(reads)

def trace(A):
    t = 0
    for i in range(min(len(A), len(A[0]))):
        t += A[i][i]
    return t

def dot(A, B, m, n):
    i = 0
    C = [[0] * m for _ in range(m)]
    reads = 0
    while i < m:
        j = 0
        while j < m:
            d = 0
            k = 0
            while k < n:
                d += A[i][k] * B[k][j]
                reads += 2
                k += 1
            C[i][j] = d
            j += 1
        i += 1
    return C, reads

def cached_dot(A, B, m, n, s):
    i = 0
    C = [[0] * m for _ in range(m)]
    reads = 0
    cache = [None] * s
    while i < m:
        j = 0
        while j < m:
            d = 0
            k = 0
            while k < n:
                d += A[i][k] * B[k][j]
                
                key_a = f'A[{i},{k}]'
                key_b = f'B[{k},{j}]'

                if not read_from_cache(cache, key_a):
                    reads += 1
                
                if not read_from_cache(cache, key_b):
                    reads += 1
                
                k += 1
            C[i][j] = d
            j += 1
        i += 1
    return C, reads

def read_from_cache(cache, key):
    print(key, end=' => ')
    print(*cache, end=' ')
    if key in cache:
        # shift left
        i = cache.index(key) + 1
        while i < len(cache) and cache[i] is not None:
            cache[i - 1] = cache[i]
            i += 1
        cache[i - 1] = key
        print('*')
        return True
    else:
        if None in cache:
            cache[cache.index(None)] = key
        else:
            cache = cache[1:]
            cache.append(key)
        print()
        return False

def read_matrix(file_name='mat1.txt'):
    with open(file_name, 'r') as f:
        line = f.readline().strip().split('.')[0]
        rows = line.split(',')
        m = [[*map(int, r.split(' '))] for r in rows]
        return m

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')