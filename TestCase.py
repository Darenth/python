import unittest
import  Upper

class Test(unittest.TestCase):
    def test_upper(self):
        text='Hello'
        result=Upper.Upper(text)
        self.assertEqual(result,'HELLO','good?')


if __name__ == '__main__':
    unittest.main()
