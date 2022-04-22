import unittest
from multiply import multiplication


class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiplication(2,3),6)
        self.assertEqual(multiplication(5,10),50)


if __name__ == '__main__':
    unittest.main()