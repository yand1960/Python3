from unittest import TestCase
from po_29_enterprize_calc.buslog.calculations import Calculations


class TestCalculations(TestCase):

    def test_plus(self):
        calculations = Calculations("log.csv")
        actual = calculations.plus(3, 4)
        self.assertEqual(7, actual)