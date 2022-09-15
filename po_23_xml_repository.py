# Создание класса-репозитория для данных, хранящихся в xml файле

import xml.etree.ElementTree as ET


class Product:

    def __init__(self, id: int, name: str, code: str, price: float):
        self.id = id
        self.name = name
        self.code = code
        self.price = price

    def __str__(self):
        return self.__dict__.__str__()


class ProductRepositoryXml:

    def __init__(self, datafile: str):
        with open(datafile, encoding="utf-8") as f:
            text = f.read()
        productsxml = ET.fromstring(text)

        self.products = []
        for p in productsxml.findall("Product"):
            id = int(p.find("ProductID").text)
            name = p.find("Name").text
            code = p.find("ProductNumber").text
            price = float(p.find("ListPrice").text)
            self.products.append(Product(id, name, code, price))

    def getbyid(self, id: int) -> Product:
        # Напишите решение в одну строку (11:03)
        return list(filter(lambda p: p.id == id, self.products))[0]

    def getbyfirstletters(self, letters: str) -> list[Product]:
        return list(filter(lambda p: p.name.upper().startswith(letters.upper()), self.products))

if __name__ == "__main__":
    repository = ProductRepositoryXml("data/Products.xml")
    # products = repository.products
    products = repository.getbyfirstletters("long")
    for p in products:
        print(f"{p.id}\t{p.name}\t{p.code}\t{p.price}")
    # print(repository.getbyid(318))

