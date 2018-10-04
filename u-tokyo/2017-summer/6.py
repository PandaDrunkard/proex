def main():
    m = 9
    n = 6
    p = 3
    s = 12

    a = zeros(m, n)
    b = zeros(n, m)

    c, reads, reads_from_ram = dot(a, b, p ,10)

    print(reads)
    print(reads_from_ram)

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

def dot(a, b, p, s):
    m = len(a)
    n = len(a[0])
    cache = Cache(s)

    c = [[0 for c in range(m)] for r in range(m)]

    u = 0
    reads = 0
    while u < m:
        v = 0
        while v < m:
            w = 0
            while w < n:
                i = u
                while i < u + p:
                    j = v
                    while j < v + p:
                        d = 0
                        k = w
                        while k < w + p:
                            cache.is_cached(f'a_{i}_{k}')
                            cache.is_cached(f'b_{k}_{j}')
                            d += a[i][k] + b[k][j]
                            reads += 2
                            k += 1
                        j += 1
                    i += 1
                w += p
            v += p
        u += p

    return c, reads, cache.read_from_ram

def trace(m):
    t = 0
    for i in range(len(m)):
        t += m[i][i]
    return t

class Cache:
    def __init__(self, s):
        self.s = s
        self.lru_list = [None for _ in range(s)]
        self.read_from_ram = 0

    def is_cached(self, key):
        cached = key in self.lru_list
        if cached == False:
            self.read_from_ram += 1

        self.__update_lru(key)

        return cached

    def __update_lru(self, key):
        if key in self.lru_list:
            idx = self.lru_list.index(key)
            for i in list(range(idx))[::-1]:
                self.lru_list[i+1] = self.lru_list[i]
        else:
            for i in list(range(self.s-1))[::-1]:
                self.lru_list[i+1] = self.lru_list[i]

        self.lru_list[0] = key

        # print(f"{key}:{self.read_from_ram}")
        # print(self.lru_list)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')