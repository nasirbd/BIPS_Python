'''
Created on Apr 15, 2016

@author: Rafi
'''
tuple1 = ('physics', 'chemistry', 1997, 2000);
# tuple1 = ['physics', 'chemistry', 1997, 2000];

def normalPrint():
    print "whole list: ", tuple1
    print "first item in the list: ", tuple1[0]
    print "tuple1[1:3]: ", tuple1[1:3]

def printUsingLoop():
    print "Using for loop"
    for i in tuple1:
        print i
    
def manipulateList():
#     tuple1.remove("physics")
#     print tuple1
#     tuple1.append("physics")
#     print tuple1
    tuple1[0] = "newValue"
    print tuple1
    print len(tuple1)
    tuple1.sort()
    print tuple1
    tuple1.reverse()
    print tuple1
    
    
if __name__ == '__main__':
    normalPrint()
    printUsingLoop()
    manipulateList()