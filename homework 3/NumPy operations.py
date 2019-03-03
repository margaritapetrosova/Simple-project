import numpy as np

class numpy:
    def __init__ (self, theNum):
        self.num=theNum
    def appendNew(self):
        print(np.append(self.num,5))
    def insertNew(self):
        print(np.insert(self.num,1,5))
    def getSqrt(self):
        print(np.sqrt(self.num))

Array1=numpy([16,25,9])
Array2=numpy([5,4,6])

Array1.appendNew()
Array2.insertNew()
Array1.getSqrt()


