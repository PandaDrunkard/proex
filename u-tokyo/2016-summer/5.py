import sys, os
import itertools

def main():
    file_path = sys.argv[1]
    content = [line.rstrip('\n') for line in open(file_path)]

    builder = Builder()
    result = builder.parse(content)
    
    print(''.join(result))

class Builder():
    SHAPES={
        '0':[
            '****', 
            '|  |', 
            '*  *',
            '|  |',
            '****',
        ],
        '1':[
            '*', 
            '|', 
            '*',
            '|',
            '*',
        ],
        '2':[
            '****', 
            '   |', 
            '*--*',
            '|   ',
            '****',
        ],
        '3':[
            '****', 
            '   |', 
            '*--*',
            '   |',
            '****',
        ],
        '4':[
            '*  *', 
            '|  |', 
            '*--*',
            '   |',
            '   *',
        ],
        '5':[
            '****', 
            '|   ', 
            '*--*',
            '   |',
            '****',
        ],
        '6':[
            '*   ', 
            '|   ', 
            '*--*',
            '|  |',
            '****',
        ],
        '7':[
            '****', 
            '   |', 
            '   *',
            '   |',
            '   *',
        ],
        '8':[
            '****', 
            '|  |', 
            '*--*',
            '|  |',
            '****',
        ],
        '9':[
            '****', 
            '|  |', 
            '*--*',
            '   |',
            '   *',
        ],
    }

    def __init__(self):
        self.lines=['' for _ in range(5)]
        self.sizes = [(5, 4), (5,2), (5, 1)]
        self.inverse_shape_dict = {}
        for key, value in Builder.SHAPES.items():
            new_key = ''.join(value)
            self.inverse_shape_dict[new_key] = key
    
    def append(self, n, space, hight):
        n = str(n)

        shape = Builder.SHAPES[n]

        # adjust hight
        while hight + len(shape) > len(self.lines):
            self.lines.append(' '*len(self.lines[0]))

        if len(self.lines[0]) > 0:
            for i, line in enumerate(self.lines):
                self.lines[i] += ' '*space
        
        for i, line in enumerate(shape):
            self.lines[hight + i] += line
        
        # 末尾を揃える
        max_len = max(map(len, self.lines))
        for i, line in enumerate(self.lines):
            if len(line) < max_len:
                self.lines[i] += ' '*(max_len - len(line))

    def __str__(self):
        return '\n'.join(self.lines)

    def parse(self, lines):
        blocks = self.predict_blocks(lines)

        return list(map(self.predict_block_shape, blocks))

    def predict_block_shape(self, block):
        scores = {}
        for num, shape in self.SHAPES.items():
            scores[num] = self.score(block ,shape)

        top = sorted(scores.items(), key=lambda i: i[1], reverse=True)[0]

        return top[0]

    def score(self, block, shape):
        if len(block[0]) in (1, 2):
            # 1
            if len(shape[0]) == 4:
                return 0
            else:
                return 1
        else:
            # 1 以外
            if len(shape[0]) == 1:
                return 0
            else:
                l1, l2 = map(''.join, [block, shape])
                matchs = sum([c1==c2 for c1, c2 in zip(l1, l2)])
                return matchs/len(l1)

    def predict_blocks(self, lines):
        delim_pos = []
        for c_idx, char in enumerate(lines[0]):
            if char == ' ':
                column = list(map(lambda line: line[c_idx], lines))
                if all(map(lambda f: f == ' ', column)):
                    delim_pos.append(c_idx)
        
        delim_pos.append(len(lines[0]))

        blocks = []
        for i, end_pos in enumerate(delim_pos):
            if i > 0:
                start_pos = delim_pos[i - 1] + 1    
            else:
                start_pos = 0

            if start_pos == end_pos:
                continue
            else:
                block = []
                for line in lines:
                    sub = line[start_pos:end_pos]
                    if ''.join(sub).strip() == '':
                        continue
                    else:
                        block.append(sub)
                blocks.append(block)

        return blocks

    def is_shape(self, block):
        for r, line in enumerate(block):
            for c, char in enumerate(line):
                if c in ('*', '|'):
                    subset = [line[max(0, c-1):c+1] for line in block[max(0, r-1):r+1]]
                    subset[1][1] = ' '
                    if ''.join(subset).strip() == '':
                        return False
        return True

    def load_block(self, lines, r, c, hight, width):
        if r + hight > len(lines):
            return None
        elif c + width > len(lines[0]):
            return None
        else:
            return list(map(lambda line: line[c:c+width], lines[r:r+hight]))

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')