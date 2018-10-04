import sys

ROME_SYMBOLS=[
    ['M' , 1000],
    ['D' ,  500],
    ['C' ,  100],
    ['L' ,   50],
    ['X' ,   10],
    ['V' ,    5],
    ['I',     1]
]

def build_symbols(symbols=ROME_SYMBOLS):
    new_symbls = []
    for i, (s, w) in enumerate(symbols):
        new_symbls.append([s, w])

        for s2, w2 in symbols[i+1:]:
            new_symbls.append([s2+s, w-w2])
    
    new_symbls = sorted(new_symbls, key=lambda i: i[1], reverse=True)

    return list(new_symbls)

NEW_ROME_SYMBOLS=build_symbols(ROME_SYMBOLS)

def to_i(inp, symbols=ROME_SYMBOLS):
    symbols = {k:v for k, v in symbols}
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

def to_r(inp, symbols=build_symbols(ROME_SYMBOLS)):
    value = int(inp)
    ret = ''

    for symbol, weight in symbols:
        while value >= weight:
            ret += symbol
            value -= weight
    
    return ret
    
def main():
    inp = sys.argv[1]

    result = to_r(inp, NEW_ROME_SYMBOLS)

    print(result)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')