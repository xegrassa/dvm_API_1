import requests

URLS = (
    'https://wttr.in/london',
    'https://wttr.in/череповец',
    'https://wttr.in/svo'
)


def main():
    payloads = {
        'lang': 'ru',
        'm': '',
    }
    for url in URLS:
        r = requests.get(url, params=payloads)
        r.raise_for_status()
        print(r.text)


if __name__ == '__main__':
    main()
