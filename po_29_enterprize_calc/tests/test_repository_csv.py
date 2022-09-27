from unittest import TestCase
from po_29_enterprize_calc.dal.repository_csv import RepositoryCsv


class TestRepositoryCsv(TestCase):

    def test_add(self):

        path = "log.csv"

        with open(path, encoding="utf-8") as f:
            expected = len(f.read().split("\n")) + 1

        repository = RepositoryCsv(path)
        repository.add(1, 2, "plus", 3)

        with open(path, encoding="utf-8") as f:
            lines = f.read().split("\n")
            actual = len(lines)
            last_string = lines[-2]

        self.assertEqual(expected, actual)
        self.assertTrue(last_string.startswith("1;2;plus;3;"))





