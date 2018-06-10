from sys import stdin
def stdinput():
    return stdin.readline().strip()

def main():
    altitutes = load_data()

    edges = create_edges(altitutes)

    # print(*edges)

    areas = calc_areas(altitutes, edges)

    print(int(sum(areas)))
    print(*([len(areas)] + [*map(int, areas)]))

def load_data():
    A = [0]
    for s in stdinput():
        if s == '\\':
            A.append(A[-1] - 1)
        elif s == '_':
            A.append(A[-1])
        elif s == '/':
            A.append(A[-1] + 1) 
    return A

def create_edges(A):
    st = [(0, None, 0)]
    highest = 0
    for i, a in enumerate(A[1:], 1):
        if st[-1][0] >= a:
            st.append((a, st[-1][2], i))
        else:
            begin = i - 1
            # NOTE: concat edges
            # this operation is performed every upforward(/) step,
            # and previous concated edges have altitute of (a - 1).
            while st[-1][1] != None and st[-1][0] == a - 1 and highest >= a:
                lev, begin, j = st.pop()
            highest = max(highest, a)
            st.append((a, begin, i))
        # print(*st)
    return [*map(lambda e: e[1:], st[1:])]

def calc_areas(A, edges):
    areas = []
    for begin, end in edges:
        area = calc_area(A, begin, end)
        if area > 0:
            areas.append(area)
    return areas    

def calc_area(A, begin, end):
    if A[begin] != A[end]:
        return 0
    b_level = A[begin]
    area = 0
    for l1, l2 in zip(range(begin, end), range(begin+1, end + 1)):
        a1 = A[l1]
        a2 = A[l2]
        area += (b_level - a1 + b_level - a2) * 1 / 2
    return area

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')