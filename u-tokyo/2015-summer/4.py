import sys

def main():
    inp = sys.argv[1]

    result = to_i(inp)

    print(result)

ROME_SYMBOLS=[
    ['M' , 1000],
    ['CM',  900],
    ['D' ,  500],
    ['CD',  400],
    ['C' ,  100],
    ['XC',   90],
    ['L' ,   50],
    ['XL',   40],
    ['X' ,   10],
    ['IX',    9],
    ['V' ,    5],
    ['IV',    4],
    ['I',     1]
]

def to_i(inp, symbols={k:v for k, v in ROME_SYMBOLS}):
    value = str(inp)
    ret = 0
    
    while len(value) > 0:
        if value[:2] in symbols:
            ret += symbols[value[:2]]
            value = value[2:]
        else:
            ret += symbols[value[0]]
            value = value[1:]

    return ret
    
if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')