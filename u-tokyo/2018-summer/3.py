import sys
import dataset as ds

def main():
    img1 = ds.image1(append_index=True)
    size = len(img1)

    bright = lambda e: e[0]**2 + e[1]**2 + e[2]**2 - e[3]/size

    by_blight = sorted(img1, key=bright)

    mean_idx = len(img1) // 2
    mean = by_blight[mean_idx]

    print(mean) # (180, 145, 72, 632252)

    # print(by_blight[mean_idx-2:mean_idx+2])

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')