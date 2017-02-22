import logging
import time
import datetime

def getlogger1():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    a=datetime.date.today().strftime("%d")+'_'+datetime.date.today().strftime("%B")+'_'+datetime.date.today().strftime("%Y")+'_'+datetime.datetime.now().strftime("%H_%M_%S")
    filename='billing_'+a+'.log'
    # create a file handler
    handler = logging.FileHandler(filename)
    handler.setLevel(logging.INFO)
 
    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
 
    # add the handlers to the logger
    logger.addHandler(handler)
    logger.info('Starting test...')    
    return logger

