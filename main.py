import requests

OFFICES = ('london', 'череповец', 'svo')


def main():
    url_params = {
        'nTqm': '',
        'lang': 'ru',
    }
    url_template = 'https://wttr.in/{}'
    for office in OFFICES:
        url = url_template.format(office)

        response = requests.get(url, params=url_params)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
