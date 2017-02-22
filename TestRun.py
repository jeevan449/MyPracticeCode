from ConfigParser import SafeConfigParser
import sqldb
import mbilling
from HTMLTestRunner import HTMLTestRunner
import unittest
import makecall
import API


#*********config parser*********#
parser = SafeConfigParser()
parser.read('config.ini')
MSISDN=parser.get('data', 'msisdn')
duration1=parser.get('billing','dur')
duration=duration1.split()
rate=float(parser.get('billing','cost'))
#*******executino starts from here*********#
class Billing(unittest.TestCase):
    def test_Billingcase1(self):
        API.updatecsv()
	a=sqldb.getDBbalance(MSISDN)
	makecall.Call(duration[0])
	b=sqldb.getDBbalance(MSISDN)
        self.assertEqual(a-b,mbilling.billingcalc(duration[0],rate))
    def test_Billingcase2(self):
        API.updatecsv()
        a=sqldb.getDBbalance(MSISDN)
        makecall.Call(duration[1])
        b=sqldb.getDBbalance(MSISDN)
        self.assertEqual(a-b,mbilling.billingcalc(duration[1],rate))
    def test_Billingcase3(self):
        API.updatecsv()
        a=sqldb.getDBbalance(MSISDN)
        makecall.Call(duration[2])
        b=sqldb.getDBbalance(MSISDN)
        self.assertEqual(a-b,mbilling.billingcalc(duration[2],rate))
    def test_Billingcase4(self):
        API.updatecsv()
        a=sqldb.getDBbalance(MSISDN)
        makecall.Call(duration[3])
        b=sqldb.getDBbalance(MSISDN)
        self.assertEqual(a-b,mbilling.billingcalc(duration[3],rate))
    def test_Billingcase5(self):
        API.updatecsv()
        a=sqldb.getDBbalance(MSISDN)
        makecall.Call(duration[4])
        b=sqldb.getDBbalance(MSISDN)
        self.assertEqual(a-b,mbilling.billingcalc(duration[4],rate))
    def test_Billingcase6(self):
        API.updatecsv()
        a=sqldb.getDBbalance(MSISDN)
        makecall.Call(duration[5])
        b=sqldb.getDBbalance(MSISDN)
        self.assertEqual(a-b,mbilling.billingcalc(duration[5],rate))
    def test_Billingcase7(self):
        API.updatecsv()
        a=sqldb.getDBbalance(MSISDN)
        makecall.Call(duration[6])
        b=sqldb.getDBbalance(MSISDN)
        self.assertEqual(a-b,mbilling.billingcalc(duration[6],rate))
    def test_Billingcase8(self):
        API.updatecsv()
        a=sqldb.getDBbalance(MSISDN)
        makecall.Call(duration[7])
        b=sqldb.getDBbalance(MSISDN)
        self.assertEqual(a-b,mbilling.billingcalc(duration[7],rate))
    def test_Billingcase9(self):
        API.updatecsv()
        a=sqldb.getDBbalance(MSISDN)
        makecall.Call(duration[8])
        b=sqldb.getDBbalance(MSISDN)
        self.assertEqual(a-b,mbilling.billingcalc(duration[8],rate))

    def test_Billingcase10(self):
        API.updatecsv()
        a=sqldb.getDBbalance(MSISDN)
        makecall.Call(duration[9])
        b=sqldb.getDBbalance(MSISDN)
        self.assertEqual(a-b,mbilling.billingcalc(duration[9],rate))
"""
    def test_Billingcase4(self):
        API.updatecsv()
        a=sqldb.getDBbalance(MSISDN)
        makecall.Call(duration[10])
        b=sqldb.getDBbalance(MSISDN)
        self.assertEqual(a-b,mbilling.billingcalc(duration[10],rate))
    def test_Billingcase4(self):
        API.updatecsv()
        a=sqldb.getDBbalance(MSISDN)
        makecall.Call(duration[11])
        b=sqldb.getDBbalance(MSISDN)
        self.assertEqual(a-b,mbilling.billingcalc(duration[11],rate))
    def test_Billingcase4(self):
        API.updatecsv()
        a=sqldb.getDBbalance(MSISDN)
        makecall.Call(duration[12])
        b=sqldb.getDBbalance(MSISDN)
        self.assertEqual(a-b,mbilling.billingcalc(duration[12],rate))
    def test_Billingcase4(self):
        API.updatecsv()
        a=sqldb.getDBbalance(MSISDN)
        makecall.Call(duration[13])
        b=sqldb.getDBbalance(MSISDN)
        self.assertEqual(a-b,mbilling.billingcalc(duration[13],rate))
    def test_Billingcase4(self):
        API.updatecsv()
        a=sqldb.getDBbalance(MSISDN)
        makecall.Call(duration[14])
        b=sqldb.getDBbalance(MSISDN)
        self.assertEqual(a-b,mbilling.billingcalc(duration[14],rate))
    def test_Billingcase4(self):
        API.updatecsv()
        a=sqldb.getDBbalance(MSISDN)
        makecall.Call(duration[15])
        b=sqldb.getDBbalance(MSISDN)
        self.assertEqual(a-b,mbilling.billingcalc(duration[15],rate))
"""
class Billing_bucket(unittest.TestCase):
    pass

class Billing_rates(unittest.TestCase):
    pass






if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite((
        loader.loadTestsFromTestCase(Billing)))
    outfile = file('Report.html', 'w')
    runner = HTMLTestRunner(stream=outfile,
                            verbosity=2,
                            title='CPS Billing Report',
                            description='************This is CPS billing test execution report********')
    runner.run(suite)
