from __future__ import print_function
import string
import random
def randstring(size,chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

class Number(object):
    def __init__(self):
        self.min=int(raw_input("minimum value of the number "))
        self.max=int(raw_input("maximum value of the number "))

    def __str__(self):
        return str(random.randint(self.min,self.max))

class String(object):
    def __init__(self):
        self.size=int(raw_input("Max length of the string "))
        self.chars=string.ascii_lowercase

    def __str__(self):
        return ''.join(random.choice(self.chars) for _ in range(self.size))

class Testcase(object):
    def __init__(self):
        self.t=int(raw_input("Enter no of test cases "))
        self.n=int(raw_input("Enter no of data items "))
        fname=raw_input("Enter the file name ")
        self.of=open(fname,'w')
        self.case=[]
        for i in range(self.n):
            x=raw_input("Data %d (N umber/ S tring) " % i )
            if x=="N":
                self.case.append(Number())
            elif x=="S":
                self.case.append(String())
            else:
                raise Exception("wrong data")
    def compute(self):
        print(self.t,file=self.of)
        for i in range(self.t):
            print(' '.join(map(str,self.case)),file=self.of)
s=Testcase()
s.compute()

