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
duration=list(parser.get('billing','dur'))
rate=float(parser.get('billing','cost'))
print duration[0],type(duration)
print rate,type(rate)
