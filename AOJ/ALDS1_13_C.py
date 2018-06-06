class Puzzle:
    WIDTH = 4
    HIGHT = 4

    def __init__(self, state):
        self.state = state

        self.zero_idx = self.state.index('0')
        self.x, self.y = self.idx_to_xy(self.zero_idx)

    def idx_to_xy(self, idx):
        return idx % Puzzle.HIGHT, idx // Puzzle.WIDTH

    def xy_to_idx(self, x, y):
        return y * Puzzle.WIDTH + x

    def swap(self, x, y):
        idx = self.xy_to_idx(x, y)
        self.state[self.zero_idx], self.state[idx] = self.state[idx], self.state[self.zero_idx]
        self.zero_idx, self.x, self.y = idx, x, y
    
    def is_completed(self):
        if self.state[-1] != '0':
            return False
        for i in range(1, 16):
            if self.state[i - 1] != str(i):
                return False
        return True
    
    def pretty_print(self):
        for r in range(Puzzle.HIGHT):
            print(self.state[r*Puzzle.WIDTH:(r+1)*Puzzle.WIDTH])

from sys import stdin
def stdinput():
    return stdin.readline().strip()

MAX_ITER = 45
def shortest_steps(p, iter, cache):
    key = ' '.join(p.state)
    if key in cache and cache[key] < 10**3:
        return cache[key]
    elif p.is_completed():
        return 0
    else:
        if iter == MAX_ITER:
            return 10**3
        else:
            steps = 10**3
            next_iter = iter + 1
            for c in list_canditee(p):
                s = shortest_steps(c, next_iter, cache)
                if s < steps:
                    steps = s
            steps += 1
            cache[key] = steps
            return steps

def list_canditee(p):
    canditees = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_x = p.x + dx
        next_y = p.y + dy
        if 0 <= next_x and next_x < p.WIDTH and 0 <= next_y and next_y < p.HIGHT:
            next_p = Puzzle(list(p.state))
            next_p.swap(next_x, next_y)
            canditees.append(next_p)
    return canditees

def main():
    puzzle = Puzzle(stdinput().split() + stdinput().split() +stdinput().split() +stdinput().split())
    steps = shortest_steps(puzzle, 0, {})
    print(steps)

if __name__ == '__main__':
    # main()
    import cProfile
    cProfile.run('main()')