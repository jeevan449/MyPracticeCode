import pyodbc



def init():
	cnxn = pyodbc.connect('DSN=my_dsn;UID=duone;PWD=duone')
	cursor = cnxn.cursor()
	return cursor

def getDBbalance(username):
	cur=init()
	user="select id from rest_subscriber where msisdn='"+username+"'"
	test=cur.execute(user)
	a=test.fetchone()
	a1=a[0]
	str1="select CREDITBALANCE,EXPIRATIONDATE from rest_rechargebin where subscriberid='"+str(a1)+"'"
	str2="select sum(CREDITBALANCE) from rest_rechargebin where subscriberid='"+str(a1)+"'"
	cur.execute(str1)
	row=cur.fetchall()
	if row:
		for i in row:
			pass
#			print i
	cur.execute(str2)
	row1=cur.fetchone()
	if row1:
		pass
		#print row1[0]
        return float(row1[0])
def getOTPDB(username):
	cur=init()
	user="select id from rest_subscriber where msisdn='"+username+"'"
	test=cur.execute(user)
	a=test.fetchone()
	a1=a[0]
	otpn="select otp FROM rest_subscribermeta where subscriberid='"+str(a1)+"'"
	b=cur.execute(otpn)
	b1=b.fetchone()
	if b1:
                pass
		#print b1[0]
        return b1[0]
