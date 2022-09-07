# Получить со страницы сайта ЦБР текущий курс доллара

from urllib import request
from http.client import HTTPResponse


def usd_rate():
    url = "http://cbr.ru/"

    response: HTTPResponse =  request.urlopen(url)
    result = response.read().decode("utf-8")
    # print(result)

    pattern = '<div class="col-md-2 col-xs-9 _dollar">USD</div>'
    position = result.find(pattern)
    result = result[position: position + 200]

    pattern = '₽'
    position = result.find(pattern)
    result = result[position - 15: position]

    pattern = '>'
    position = result.find(pattern)
    result = result[position + 1: ].strip(" ").replace(",", ".")

    return float(result)


if __name__ == "__main__":
    print(usd_rate() * 2)

