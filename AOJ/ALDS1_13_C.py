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

MAX_ITER = 20
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def shortest_steps(p, iter, cache):
    key = ' '.join(p.state)
    if p.is_completed():
        return 0
    else:
        if iter == MAX_ITER:
            return 10**3
        else:
            min_next_steps = 10**3
            next_iter = iter + 1
            if key in cache:
                this_cache = cache[key]
            else:
                this_cache = {}
                cache[key] = this_cache
            
            for dd in DIRECTIONS:
                if dd in this_cache and this_cache[dd] < 10**3:
                    next_steps = this_cache[dd]
                else:
                    next_x = p.x + dd[0]
                    next_y = p.y + dd[1]
                    if 0 <= next_x and next_x < p.WIDTH and 0 <= next_y and next_y < p.HIGHT:
                        next_p = Puzzle(list(p.state))
                        next_p.swap(next_x, next_y)
                        next_steps = shortest_steps(next_p, next_iter, cache)
                        this_cache[dd] = next_steps
                    else:
                        next_steps = 10**3
                if next_steps < min_next_steps:
                    min_next_steps = next_steps
            steps = min_next_steps + 1
            return steps

def main():
    puzzle = Puzzle(stdinput().split() + stdinput().split() +stdinput().split() +stdinput().split())
    steps = shortest_steps(puzzle, 0, {})
    print(steps)

if __name__ == '__main__':
    # main()
    import cProfile
    cProfile.run('main()')