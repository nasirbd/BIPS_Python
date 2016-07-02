'''
Created on Apr 15, 2016

@author: Rafi
'''

class TestClass:
    i = 5
    def __init__(self):
        self.forLoop1()
        self.forLoop2()

    def forLoop1(self):
#         i = 10
        print self.i
        count = 10
        for i in range(0, count):
            print "i: ", i
            
    def forLoop2(self):
        a = ["Bangladesh", "Sweden", "France"]
        for i in a:
            print "i: ", i
    

if __name__ == '__main__':
    instance1 = TestClass();