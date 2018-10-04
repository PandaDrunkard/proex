def main():
    mat1 = load_mat('./2018-summer/mat1.txt')    
    mat2 = load_mat('./2018-summer/mat2.txt')
    
    mat3, reads = dot(mat1, mat2)
    tra = trace(mat3)
    print(tra)
    

def zeros(m, n):
    return [[0 for c in range(n)] for r in range(m)]

def load_mat(file_name):
    with open(file_name) as f:
        line = f.readlines()[0]
    
    line = line.strip()
    rows = line.split('.')[0].split(',')
    rows = [r.split(' ') for r in rows]

    m = len(rows)
    n = len(rows[0])

    mat = zeros(m, n)

    for i in range(m):
        for j in range(n):
            mat[i][j] = int(rows[i][j])
    
    return mat

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

def trace(m):
    t = 0
    for i in range(len(m)):
        t += m[i][i]
    return t

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')