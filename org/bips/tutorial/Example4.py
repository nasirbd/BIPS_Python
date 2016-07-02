'''
Created on Apr 15, 2016

@author: Rafi
'''

import datetime
import os

def normalPrint():
    today = datetime.date.today()
    print "Today's date is: " + str(today)
    
def printCurrentWorkingDirectory():
    print os.getcwd()
    
if __name__ == '__main__':
    normalPrint()
    printCurrentWorkingDirectory()