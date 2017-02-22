import csv
import hashlib
import requests
import sys
import subprocess
from datetime import datetime
import math
import time
import pyodbc
import sqldb

Rate=float(sys.argv[3])
Duration=sys.argv[1]
Number=str(sys.argv[2])
CPSIP='192.168.4.48'
Port='5060'
LBIP='192.168.4.193'
MSISDN='91000000508'
IMSI='123123123'
IMEI='3213212321'


def roundup(x):
    return (math.ceil((x) / 60.0)) * 60

def billingcalc(dur,rate):
	dur1=roundup(float(dur))
	cost=dur1*rate
	ccsot=cost/60
	return ccsot

def getBalancenew(MSISDN,IMSI,IMEI):
	# print MSISDN,IMSI,IMEI
	URL='http://192.168.4.188:9292/api/getbalance?HTTP_X_MSISDN='+MSISDN+'&HTTP_X_IMSI='+IMSI+'&HTTP_X_IMEI='+IMEI
	req = requests.request('GET', URL)
	return req.text

def getToken(MSISDN,IMSI,IMEI):
	URL='http://192.168.4.188:9292/api/gettoken?HTTP_X_MSISDN='+MSISDN+'&HTTP_X_IMSI='+IMSI+'&HTTP_X_IMEI='+IMEI
	req = requests.request('GET', URL)
	names = [item['token'] for item in req.json()]
	token=names[0]
	return token

def InsertData(password):
	list1=[]
	list1.insert(0,password)
	#print list1
	with open('call.csv', 'wb') as csvfile:
	    spamwriter = csv.writer(csvfile,quoting=csv.QUOTE_MINIMAL)
	    spamwriter.writerow(['SEQUENTIAL'] * 1)
	    spamwriter.writerow(list1)

def waitfun(dur1):
    dur2=float(dur1)+7 
    time.sleep(dur2)

def makeCall(dur):
    print "Call Duration is..."+dur+".....and",
    print "Start time..."+str(datetime.now())
    print "Balance from API before call...=",
    b=getBalancenew(MSISDN,IMSI,IMEI)
    print b
    command="./sipp "+LBIP+":"+Port+" -sf CPS1.xml -inf call.csv -i 192.168.4.194 -p 9921 -m 1 -d "+dur+"s"+" -bg"
    #print command
    status= subprocess.call(command, shell=True, stdout=subprocess.PIPE)
    waitfun(dur)
    print "Balance from API after call.....=",
    time.sleep(2)
    a=getBalancenew(MSISDN,IMSI,IMEI)
    print a
    #print "**********Total Cost API ********"
    #print float(b)-float(a)
    


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
finalstring=""
finalstring=Number+";[authentication username="+MSISDN+" password="+updatedpw+"];"+MSISDN+";"
#print finalstring
#print "duration is  "+Duration
print "Making Call from User.........."+MSISDN
InsertData(finalstring)
a=sqldb.getDBbalance(MSISDN)
makeCall(Duration)
b=sqldb.getDBbalance(MSISDN)
print "call cost from DB is...:",
print float(a)-float(b)
print "Manual Biling duration is ......=",
print billingcalc(Duration,Rate)
