import unittest

from pi_by_hand import PiCalculator


class PiByHandTestCase(unittest.TestCase):

    def setUp(self):
        self.pi_calculator = PiCalculator(4)

    def test_div_one_by_integer_5(self):

        self.assertEqual(self.pi_calculator.divide_one_by(5), '0.200')

    def test_div_one_by_integer_3(self):

        self.assertEqual(self.pi_calculator.divide_one_by(3), '0.333')

    def test_add_two_strings(self):

        self.assertEqual(self.pi_calculator.add_two_strings('0.123', '0.999'), '1.122')

    def test_sub_two_strings(self):

        self.assertEqual(self.pi_calculator.sub_two_strings('0.888', '0.121'), '0.767')

    def test_multiply_string_by_four(self):
        self.assertEqual(self.pi_calculator.multiply_string_by_four('0.555'), '2.220')
