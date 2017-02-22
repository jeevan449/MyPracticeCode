import csv
import hashlib
import requests
import time
from ConfigParser import SafeConfigParser
import sqldb
from random import randint

#*********config parser*********#
parser = SafeConfigParser()
parser.read('config.ini')
ip=parser.get('data', 'mpsip')
port=parser.get('data','mpsport')
MSISDN=parser.get('data','msisdn')
IMSI=parser.get('data','imsi')
IMEI=parser.get('data','imei')
Rate=parser.get('billing','rate')



def getBalancenew(MSISDN,IMSI,IMEI):
        URL='http://'+ip+':'+port+'/api/getbalance?HTTP_X_MSISDN='+MSISDN+'&HTTP_X_IMSI='+IMSI+'&HTTP_X_IMEI='+IMEI
        req = requests.request('GET', URL)
        return req.text

def getToken(MSISDN,IMSI,IMEI):
        try:
            URL='http://'+ip+':'+port+'/api/gettoken?HTTP_X_MSISDN='+MSISDN+'&HTTP_X_IMSI='+IMSI+'&HTTP_X_IMEI='+IMEI
            req = requests.request('GET', URL)
            names = [item['token'] for item in req.json()]
            token=names[0]
            return token
	except Exception as e: 
	    print e
   


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def updatecsv():
    str2= str(getToken(MSISDN,IMSI,IMEI))
    str1= MSISDN
    str3=str(sqldb.getOTPDB(MSISDN))
    password=str1+str2+str3
    m = hashlib.md5()
    m.update(password)
    updatedpw=m.hexdigest()
    strtest=""
    strtest=updatedpw
    #print updatedpw
    Number=Rate+str(random_with_N_digits(10))
    finalstring=""
    finalstring=Number+";[authentication username="+MSISDN+" password="+updatedpw+"];"+MSISDN+";"
    list1=[]
    list1.insert(0,finalstring)
    #print list1
    with open('call.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile,quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['SEQUENTIAL'] * 1)
        spamwriter.writerow(list1)

