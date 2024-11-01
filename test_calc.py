import calc
import unittest

class CalcTest(unittest.TestCase):
    def test_add1(self):
        self.assertEqual(calc.add(1,2,), 3)

    # def  test_add2(self):
    #     self.assertNotEqual(calc.add(2, 3), 5)

if __name__ == '__main__':
    print('start!')