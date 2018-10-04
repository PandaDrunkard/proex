import sys
import dataset as ds

def main():
    img = ds.image2(append_index=True)
    img = ds.format_square(img)

    ds.save_image('image2.tif', img)


if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')