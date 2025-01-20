import unittest
from ex4 import set_age, NegativeAgeError

class TestNegativeNumber(unittest.TestCase):
    def test_negative(self):
        with self.assertRaises(NegativeAgeError):
            set_age(-1)

if __name__ == '__main__':
    unittest.main()

