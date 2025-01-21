import unittest
from conversion import dollars_to_dirhams, meters_to_kilometers


class TestConversionFunctions(unittest.TestCase):
    def test_dollars_to_dirhams(self):
        self.assertAlmostEqual(dollars_to_dirhams(1), 10.02)
        self.assertAlmostEqual(dollars_to_dirhams(0), 0.0)

    def test_meters_to_kilometers(self):
        self.assertEqual(meters_to_kilometers(1000), 1.0)
        self.assertEqual(meters_to_kilometers(0), 0.0)

if __name__ == '__main__':
    unittest.main()
