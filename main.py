import requests

URL = 'https://wttr.in/san%20francisco?nTqu&lang=en'


def main():
    r = requests.get(URL)
    r.raise_for_status()
    print(r.text)


if __name__ == '__main__':
    main()
