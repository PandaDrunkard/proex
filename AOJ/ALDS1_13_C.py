class Puzzle:
    def __init__(self, state):
        self.WIDTH = 4
        self.HIGHT = 4

        self.state = state
        self.x, self.y = self.idx_to_xy(self.state.index('0'))

    def idx_to_xy(self, idx):
        return idx % self.HIGHT, idx // self.WIDTH

    def xy_to_idx(self, x, y):
        return y * self.WIDTH + x

    def swap(self, c1, c2):
        idx1 = self.xy_to_idx(*c1)
        idx2 = self.xy_to_idx(*c2)
        tmp = self.state[idx1]
        self.state[idx1] = self.state[idx2]
        self.state[idx2] = tmp
    
    def is_completed(self):
        for i in range(1, 15):
            if self.state[i - 1] != str(i):
                return False
        return True

from sys import stdin
def stdinput():
    return stdin.readline().strip()

def main():
    puzzle = Puzzle(stdinput().split() + stdinput().split() +stdinput().split() +stdinput().split())


if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')