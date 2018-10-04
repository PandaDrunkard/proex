import requests
from bs4 import BeautifulSoup

def main(n):
    from time import sleep
    for idx in range(1, n + 1):
        extract_title(idx, f"https://projecteuler.net/problem={idx}")
        sleep(1)

def extract_title(idx, url):
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'lxml')
        title = soup.find_all("h2")[0].text
    except:
        title = 'ERROR'

    print(f'Problem {idx} - {title}')


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = 10
    main(n)
    # import cProfile
    # cProfile.run('main()')