from sys import stdin
def stdinput():
    return stdin.readline().strip()

class Card:
    def __init__(self, value):
        self.value = int(value[1:])
        self.value2 = value

def main():
    n = int(stdinput())
    A = list(map(Card, stdinput().split()))

    bubble_sorted = bubble_sort(A[:], len(A))
    selection_sorted = selection_sort(A[:], len(A))

    print(' '.join(map(lambda c: c.value2, bubble_sorted)))
    print('Stable' if is_stable(A, bubble_sorted) else 'Not stable')
    print(' '.join(map(lambda c: c.value2, selection_sorted)))
    print('Stable' if is_stable(A, selection_sorted) else 'Not stable')


def bubble_sort(A, N):
    for i in range(N):
        for j in range(N-1, i, -1):
            if A[j].value < A[j-1].value:
                A[j], A[j-1] = A[j-1], A[j]
    return A

def selection_sort(A, N):
    for i in range(N):
        min_idx = i
        for j in range(i+1, N):
            if A[j].value < A[min_idx].value:
                min_idx = j
        if min_idx != i:
            A[i], A[min_idx] = A[min_idx], A[i]
    return A

def is_stable(A, B):
    for i in range(1, 10):
        sub_A = list(filter(lambda c: c.value == i, A))
        sub_B = list(filter(lambda c: c.value == i, B))
        for a, b in zip(sub_A, sub_B):
            if a.value2 != b.value2:
                return False
    return True

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')