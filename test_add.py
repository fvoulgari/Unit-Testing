import unittest
from add import addition


class TestAdd(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(addition(2,3),5)
        self.assertEqual(addition(-1,-1),-2 )
        self.assertEqual(addition(-1,1),0 )
        self.assertEqual(addition(-1,2), 1)



if __name__ == '__main__':
    unittest.main()