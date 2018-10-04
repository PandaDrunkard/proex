import sys
import dataset as ds

def sort_by_bright(img):
    size = len(img)
    # use index as a bright adjuster for images of same brightness
    bright = lambda e: e[0]**2 + e[1]**2 + e[2]**2 - e[3]/size
    by_blight = sorted(img, key=bright)

    return list(by_blight)

def main(k=2):
    img2 = ds.image2(append_index=True)
    img2 = sort_by_bright(img2)
    n = len(img2)
    # print(n)
    
    elements = []
    for i in range(k):
        idx = n * i // k
        elements.append(img2[idx])
        print(elements[-1])
    
    # print(img2[0])
    # print(img2[40000])
    # print(img2[80000])
    # print(img2[120000])

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')