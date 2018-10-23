import unittest
from powerApp.power import power
class Powertest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(power(1,1),1)
    
    def test_power(self):
        self.assertEqual(power(2,2),4)
        self.assertEqual(power(2,3),8)
        self.assertEqual(power(2,4),16)
if __name__ == "main":
    unittest.main()
