import unittest
from po_07_functions import plus, minus
from po_23_xml_repository import ProductRepositoryXml, Product


class TestPo08(unittest.TestCase):

    def test_plus(self):
        x = [1, 123, 100000]
        y = [1, 256, 2]
        expected = [2, 379, 100002]
        for i in range(0, len(x)):
            result = plus(x[i], y[i])
            self.assertEqual(expected[i], result)

    def test_minus(self):
        x = 1
        y = 2
        expected = -1
        result = minus(x, y)
        self.assertEqual(expected, result)


class TestProductRepositoryXml(unittest.TestCase):

    def setUp(self):
        self.repository = ProductRepositoryXml("data/ProductsTesting.xml")

    def test_products(self):
        products = self.repository.products
        self.assertEqual(254, len(products))
        p = products[123]
        self.assertEqual(869, p.id)
        self.assertEqual("Women's Mountain Shorts, L", p.name)
        self.assertEqual("SH-W890-L", p.code)
        self.assertEqual(83.36, p.price)

    def test_getbyid(self):
        p = self.repository.getbyid(869)
        self.assertEqual(869, p.id)
        self.assertEqual("Women's Mountain Shorts, L", p.name)
        self.assertEqual("SH-W890-L", p.code)
        self.assertEqual(83.36, p.price)

    def test_getbyfirstletters(self):
        products = self.repository.getbyfirstletters("re")
        self.assertEqual(2, len(products))
        p = products[1]
        self.assertEqual(907, p.id)
        self.assertEqual("Rear Brakes", p.name)
        self.assertEqual("RB-9231", p.code)
        self.assertEqual(126.84, p.price)

    def tearDown(self):
        print("Этот метод должен откатить изменения, внесенные тестами")
