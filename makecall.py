from ConfigParser import SafeConfigParser
import time
import subprocess
import logger

parser = SafeConfigParser()
parser.read('config.ini')
ip=parser.get('data', 'sippip')
port=parser.get('data','sippport')
LBIP=parser.get('data','lbip')
Port='5060'


def waitfun(dur1):
    dur2=float(dur1)+7
    time.sleep(dur2)

def Call(dur):
    try:
        command="./sipp "+LBIP+":"+Port+" -sf CPS1.xml -inf call.csv -i "+ip+" -p "+port+" -m 1 -d "+dur+"s"+" -bg -trace_err"
        status= subprocess.call(command, shell=True, stdout=subprocess.PIPE)
        waitfun(dur)
        time.sleep(5)
    except Exception as e: 
	print e
