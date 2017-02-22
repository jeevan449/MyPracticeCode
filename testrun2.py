import unittest
import HTMLTestRunner
from ConfigParser import SafeConfigParser
import sqldb
import mbilling
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
    pass    
def test_generator(dur):
    def test(self):
        API.updatecsv()
        a=sqldb.getDBbalance(MSISDN)
	print a
        makecall.Call(dur)
        b=sqldb.getDBbalance(MSISDN)
	print b
        c=format(a-b, '.2f')
        m1=mbilling.billingcalc(dur,rate)
        m2=format(m1, '.2f')
        self.assertEqual(float(c),float(m2))
    return test



if __name__ == '__main__':
    for i in range(len(duration)):
	test_name='test_%s_sec_duration' %duration[i]
	test =test_generator(duration[i])
	setattr(Billing,test_name,test)
    HTMLTestRunner.main()
