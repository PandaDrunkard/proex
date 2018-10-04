import sys, os

def main():
    fields = sys.argv[1].split(',')

    numbers = fields[0]
    hights = list(map(int, fields[1::2]))
    spaces = [0] + list(map(int, fields[2::2])) # [0] for first number

    builder = Builder()

    for n, space, hight in zip(numbers, spaces, hights):
        builder.append(n, space, hight)

    print(str(builder))

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
        self.sizes = [(5, 4), (5, 1)]
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
        # grid search
        line = lines[0]
        parsed = [False for _ in lines[0]]
        ret = []
        for c, char in enumerate(line):
            if char != '*' or parsed[c] == True:
                continue

            for size in self.sizes:
                block = self.load_block(lines, c, size[1])
                result = self.parse_block(block)
                if result == None:
                    continue
                else:
                    for w in range(size[1]):
                        parsed[c+w] = True
                    break
            
            if result != None:
                ret.append(result)
        
        return ret

    def load_block(self, lines, c, width):
        if c + width > len(lines[0]):
            return None
        else:
            return list(map(lambda line: line[c:c+width], lines))
    
    def parse_block(self, block):
        if block == None:
            return None
        
        key = ''.join(block)
        if key in self.inverse_shape_dict:
            return self.inverse_shape_dict[key]
        else:
            return None

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')