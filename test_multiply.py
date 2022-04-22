import unittest
from multiply import multiplication


class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiplication(2,3),6)
        self.assertEqual(multiplication(-1,-1),1 )
        self.assertEqual(multiplication(-1,1),-1)



if __name__ == '__main__':
    unittest.main()