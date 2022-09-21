from urllib import request
from http.client import HTTPResponse
import json
from po_21_urllib import CbrRate


class CbrData(CbrRate):

    def __init__(self):
        self.url_ws = "https://www.cbr-xml-daily.ru/daily_json.js"
        super().__init__()

    def rate(self, currency):

        response: HTTPResponse = request.urlopen(self.url_ws)
        result = response.read().decode("utf-8")
        # print(result)

        rates = json.loads(result)
        return rates['Valute'][currency]['Value']


if __name__ == "__main__":
    cbr = CbrData()
    print(cbr.rate("USD"), cbr.rate("AZN"), cbr.usd_rate())
