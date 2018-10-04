import math

def load_image(filename, append_index=False):
    content = [line.strip().split(' ') for line in open(filename)][0]
    r = list(map(int, content[0::3]))
    g = list(map(int, content[1::3]))
    b = list(map(int, content[2::3]))
    if append_index:
        return list(zip(r,g,b,range(len(r))))
    else:
        return list(zip(r,g,b,))

WHITE=tuple([255,255,255])
def format_image(raw):
    formated = [[]]
    for i, element in enumerate(raw):
        if element[:3] == WHITE:
            subset = raw[i::i+1]
            is_white_line = (len(subset) > 2)
            for sub in raw[i::i+1]:
                if sub[:3] != WHITE:
                    is_white_line = False
                    break
            if is_white_line:
                formated.append([])
            else:
                formated[-1].append(element)
        else:
            formated[-1].append(element)
    formated = formated[:-1]
    return formated

def format_square(raw):
    size = len(raw)
    w = int(math.sqrt(size))
    formatted = []
    for i in range(len(raw) // w):
        formatted.append([])
        for j in range(w):
            formatted[-1].append(raw[i*w + j])
    return formatted

def width(raw):
    size = len(raw)
    for i in range(1, size//2):
        rgb = raw[i][:3]
        if rgb == WHITE:
            subset = raw[i::i+1]
            # print(f'{(i+1)}: {subset[:5]}')
            is_white = map(lambda subelm: subelm[:3]==WHITE, subset)
            if all(is_white):
                return i+1
    return -1

def format_image2(raw):
    w = width(raw)
    formatted = []
    for i in range(len(raw) // w):
        formatted.append([])
        for j in range(w):
            formatted[-1].append(raw[i*w + j])
    return formatted

def test(append_index=False):
    return load_image('./test.txt', append_index=append_index)
def image1(append_index=False):
    return load_image('./image1.txt', append_index=append_index)
def image2(append_index=False):
    return load_image('./image2.txt', append_index=append_index)
def image3(append_index=False):
    return load_image('./image3.txt', append_index=append_index)

TIF_HEADER_ARRAY=[
    77,77, 0,42, 0,  0, 0, 8, 0, 7, 1, 0, 0, 4, 0, 0,
     0, 1, 0, 0, 0,  0, 1, 1, 0, 4, 0, 0, 0, 1, 0, 0,
     0, 0, 1, 2, 0,  3, 0, 0, 0, 3, 0, 0, 0,98, 1, 6,
     0, 3, 0, 0, 0,  1, 0, 2, 0, 0, 1,17, 0, 4, 0, 0,
     0, 1, 0, 0, 0,104, 1,21, 0, 3, 0, 0, 0, 1, 0, 3,
     0, 0, 1,23, 0,  4, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 8, 0,  8, 0, 8
]
def save_image(filename, image):
    hight = len(image)
    width = len(image[0])

    b_hight = (hight).to_bytes(4, byteorder='big')
    b_width = (width).to_bytes(4, byteorder='big')
    b_s = (hight*width*3).to_bytes(4, byteorder='big')

    # set hight/width/s
    header = TIF_HEADER_ARRAY[:]
    for i in range(4):
        header[18 + i] = b_width[i]
        header[30 + i] = b_hight[i]
        header[90 + i] = b_s[i]
    b_header = bytes(header)

    content = []
    for r in range(hight):
        for c in range(width):
            content += list(image[r][c][:3])
    b_content = bytes(content)

    with open(filename, 'wb') as out:
        out.write(b_header)
        out.write(b_content)