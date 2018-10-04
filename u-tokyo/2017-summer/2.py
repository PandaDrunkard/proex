def main():
    mat = load_mat('./2018-summer/mat1.txt')
    print(mat)

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

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')