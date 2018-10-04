import sys, os

def main():
    file_path = sys.argv[1]
    content = [line.strip() for line in open(file_path)]

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
        self.sizes = [(5, 4), (5, 1)]
        self.inverse_shape_dict = {}
        for key, value in Builder.SHAPES.items():
            new_key = ''.join(value)
            self.inverse_shape_dict[new_key] = key
    
    def append(self, n):
        n = str(n)
        # assert n in Builder.SHAPES

        shape = Builder.SHAPES[n]

        if len(self.lines[0]) > 0:
            for i, line in enumerate(self.lines):
                self.lines[i] += ' '*2
        
        for i, line in enumerate(shape):
            self.lines[i] += line

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