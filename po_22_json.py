from urllib import request
from http.client import HTTPResponse
import json


def rate(currency):
    url = "https://www.cbr-xml-daily.ru/daily_json.js"

    response: HTTPResponse =  request.urlopen(url)
    result = response.read().decode("utf-8")
    # print(result)

    rates = json.loads(result)
    return rates['Valute'][currency]['Value']


if __name__ == "__main__":
    print(rate("USD"), rate("AZN"))