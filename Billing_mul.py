import json
import csv
import hashlib
import requests
import sys
import subprocess
from datetime import datetime
import math
import time
from termcolor import colored
import sqldb

#Rate=float(sys.argv[2])
#Duration=sys.argv[1]
#Number=str(sys.argv[1])
CPSIP='192.168.4.48'
Port='5060'
LBIP='192.168.4.193'
MSISDN='91000000607'
IMEI='3213212321'
IMSI='123123123'
sippport=7685
MPSIP='192.168.4.188'
MPSPort='9292'

def roundup(x):
    return (math.ceil((x) / 60.0)) * 60

def billingcalc(dur,rate):
	dur1=roundup(float(dur))
	cost=dur1*rate
	ccsot=cost/60
        log("manula caluculation....")
        log(ccsot)
	return ccsot

def getBalancenew(MSISDN,IMSI,IMEI):
	# print MSISDN,IMSI,IMEI
	URL='http://'+MPSIP+':'+MPSPort+'/api/getbalance?HTTP_X_MSISDN='+MSISDN+'&HTTP_X_IMSI='+IMSI+'&HTTP_X_IMEI='+IMEI
	req = requests.request('GET', URL)
	a=json.loads(req.text)
        b=a[0]
        return b["balance"]
def getCost(MSISDN,IMSI,IMEI,Number):
	URL='http://'+MPSIP+':'+MPSPort+'/api/costtocountry/'+Number+'?HTTP_X_MSISDN='+MSISDN+'&HTTP_X_IMSI='+IMSI+'&HTTP_X_IMEI='+IMEI
        req = requests.request('GET', URL)
        a=json.loads(req.text)
        b=a[0]
        return b["debitcost"]


def getToken(MSISDN,IMSI,IMEI):
	URL='http://'+MPSIP+':'+MPSPort+'/api/gettoken?HTTP_X_MSISDN='+MSISDN+'&HTTP_X_IMSI='+IMSI+'&HTTP_X_IMEI='+IMEI
	req = requests.request('GET', URL)
	names = [item['token'] for item in req.json()]
	token=names[0]
	return token

def InsertData(password):
	list1=[]
	list1.insert(0,password)
	#print list1
	with open('cps1.csv', 'wb') as csvfile:
	    spamwriter = csv.writer(csvfile,quoting=csv.QUOTE_MINIMAL)
	    spamwriter.writerow(['SEQUENTIAL'] * 1)
	    spamwriter.writerow(list1)

def log(data):
        list1=[]
        list1.insert(0,data)
        with open('auto.csv', 'ab') as csvfile:
            spamwriter = csv.writer(csvfile,quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(list1)

def waitfun(dur1):
    dur2=int(dur1)+10
    time.sleep(dur2)

def makeCall(dur):
    global sippport
    print "Call Duration is..."+str(dur)
    log("Call Duration is..."+str(dur))
    print "Start time..."+str(datetime.now())
    log("Start time..."+str(datetime.now()))
    print "Balance from API before call"
    log("Balance from API before call")
    b=getBalancenew(MSISDN,IMSI,IMEI)
    print b
    log(b)
    print "Balance from DB....=",
    bdb=sqldb.getDBbalance(MSISDN)
    print bdb
    log(bdb)
    log(b)
    command="./sipp "+LBIP+":"+Port+" -sf CPS_mulbilling.xml -inf cps1.csv -i 192.168.4.194 -p "+str(sippport)+" -m 1 -d "+str(dur)+"s"+" -bg -trace_err"
    #print command
    sippport+=1
    subprocess.call(command, shell=True, stdout=subprocess.PIPE)
    waitfun(dur)
    print "Balance from API after call"
    time.sleep(2)
    a=getBalancenew(MSISDN,IMSI,IMEI)
    print a
    print "Balance from DB....=",
    adb=sqldb.getDBbalance(MSISDN)
    log(a)
    log(adb)
    print "**********Total Cost API ********"
    log("**********Total Cost API ********")
    autocost=float(b)-float(a)
    print autocost
    log(float(b)-float(a))
    print ".........Total cost from DB.........."
    log(float(bdb)-float(adb))
    return autocost
    

def getUpdatedPW(Num):
    str2= str(getToken(MSISDN,IMSI,IMEI))
    str1= MSISDN
    str3='5719'
    password=str1+str2+str3
    m = hashlib.md5()
    m.update(password)
    updatedpw=m.hexdigest()
    strtest=""
    strtest=updatedpw
    #print updatedpw
    finalstring=""
    finalstring=str(Num)+";[authentication username="+MSISDN+" password="+updatedpw+"];"+MSISDN+";"
    #print finalstring
    #print "duration is  "+Duration
    print "Making Call from User.........."+MSISDN
    log("Making Call from User.........."+MSISDN)
    return finalstring

def start1():
    log("**************start***************")
    print colored('**********Executing test**************','magenta')

def stop1():
    log("**************stop*************")
    print colored('**************Completed test****************','magenta')
def main():
    lst1=[12,58,143,46,600,1803,23]
    lst2=[93242342234,9732342234,8802342234,12342234,862342234,202342234,2512342234,912342234,982342234,9622342234,2542342234,9652342234,9612342234,2122342234,9772342234,2342342234,9682342234,922342234,9702342234,632342234,9742342234,9662342234,2112342234,942342234,2492342234,9632342234,662342234,2162342234,442342234,9672342234]
    lst3=[1.2,0.6,0.16,1.25,0.15,0.38,1,0.14,1,0.6,1.25,0.6,1,2,0.4,1.25,0.6,0.1,1,0.5,0.6,0.6,9,0.45,0.6,1,1.25,9,1.25,0.6]
    for i in lst1:
        for j,k in zip(lst2,lst3):
            start1()
            InsertData(getUpdatedPW(j))
            print "rate is..... "+str(k)#+"APIrate...."+str(getCost(MSISDN,IMSI,IMEI,str(j))
            print "Dialing number is.... "+str(j)
            time.sleep(1)
            autob= makeCall(i)
            print "Manual Biling duration is ............."
            manb= billingcalc(i,k)
            print manb
            if(str(manb) == str(autob)):
                print colored("Pass ...duration is"+str(i),'green')
            else:
                print colored("Failed ...duration is"+str(i),'red')
            stop1()

if __name__== "__main__":
    main()
