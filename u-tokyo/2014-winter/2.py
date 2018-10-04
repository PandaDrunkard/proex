def func(n):
    f1, f2 = 1, 1
    remains = n

    while remains > 2:
        f1, f2 = f1+f2, f1
        remains -= 1
    
    return f1

def main():
    f50 = func(50)

    print(f50)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')