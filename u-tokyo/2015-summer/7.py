def stdinput():
    from sys import stdin
    return stdin.readline().strip()

def main():
    words = stdinput().split(' ')

    n = parse(words)

    print(n)

SYMBOLS={
    'one':         1,
    'two':         2,
    'three':       3,
    'four':        4,
    'five':        5,
    'six':         6,
    'seven':       7,
    'eight':       8,
    'nine':        9,
    'ten':        10,
    'eleven':     11,
    'twelve':     12,
    'thriteen':   13,
    'fourteen':   14,
    'fifteen':    15,
    'sixteen':    16,
    'seventeen':  17,
    'eighteen':   18,
    'ninteen':    19,
    'twenty':     20,
    'thirty':     30,
    'fourty':     40,
    'fifty':      50,
    'sixty':      60,
    'seventy':    70,
    'eighty':     80,
    'ninty':      90,
}

def parse(words, symbols=SYMBOLS):
    thousand, hundred, one = divide_words(words)

    if len(thousand) == 0 and len(hundred) == 0:
        n = 0
        for token in words:
            n += symbols[token]
        return n
    else:
        return parse(thousand) * 1000 + parse(hundred) * 100 + parse(one)

def divide_words(words):
    thousand = []
    hundred = []
    one = []

    if 'thousand' in words:
        while words[0] != 'thousand':
            thousand.append(words[0])
            words = words[1:]
        words = words[1:]
    
    if 'hundred' in words:
        while words[0] != 'hundred':
            hundred.append(words[0])
            words = words[1:]
        words = words[1:]
    
    one = words

    return thousand, hundred, one

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')