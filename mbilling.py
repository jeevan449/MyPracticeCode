import math
import logger


def roundup(x):
    return (math.ceil((x) / 60.0)) * 60

def billingcalc(dur,rate):
        dur1=roundup(float(dur))
        cost=dur1*rate
        ccsot=cost/60
        return ccsot
