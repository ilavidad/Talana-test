import unittest
from blazer import productPurchase

def suite():
    suite = unittest.TestSuite()
    suite.addTest(productPurchase('buy'))
    #suite.addTest(productPurchase('SingUp'))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)