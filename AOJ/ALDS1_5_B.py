from sys import stdin, maxsize


def stdinput():
    return stdin.readline().strip()

def main():
    n = int(stdinput())
    *A, = map(int, stdinput().split(' '))
    o = mergeSort(A, 0, n)

    print(*A)
    print(o)

def merge(A, left, mid, right):
    L = A[left:mid]
    R = A[mid:right]

    cap = maxsize
    L.append(cap)
    R.append(cap)

    i = j = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return i + j

def mergeSort(A, left, right):
    o = 0
    if left + 1 < right:
        mid = (left + right) // 2
        o += mergeSort(A, left, mid)
        o += mergeSort(A, mid, right)
        o +=  merge(A, left, mid, right)
    return o

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')