import sys
import dataset as ds

def main():
    img1 = ds.image1()
    img1 = ds.format_image2(img1)

    hight = len(img1)
    width = len(img1[0])

    print(width)
    # print(hight)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')