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
duration=['10']
rate=0.5
IMSI=parser.get('data','imsi')
IMEI=parser.get('data','imei')
#*******executino starts from here*********#
#a=sqldb.getDBbalance(MSISDN)
#print a
#print type(a)
print API.getBalancenew(MSISDN,IMSI,IMEI)
