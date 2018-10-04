import sys
import dataset as ds

def main():
    img1 = ds.test()
    print(len(img1)) # 960000

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')