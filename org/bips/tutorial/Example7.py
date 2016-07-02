'''
Created on Apr 15, 2016

@author: Rafi
'''

from Example4 import normalPrint

if __name__ == '__main__':
    
    normalPrint()               # will work
    printCurrentWorkingDirectory()       # will not work
    
    Example4.normalPrint()       # will not work
    Example4.printCurrentWorkingDirectory()     # will not work