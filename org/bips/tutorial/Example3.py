'''
Created on Apr 15, 2016

@author: Rafi
'''

def normalPrint():
    print "inside the method"
    print __name__, " here"
    
if __name__ == '__main__':
    print "calling method from main()"
    print __name__
    normalPrint()