'''
Created on Apr 4, 2009

@author: mturner
'''
import util

t = util.Timer()
t.start()

nResult = 1
dResult = 1

for i in range(10,100):
    for j in range(i,100):
        match = False
        (nTens, nOnes) = divmod(i, 10)
        (dTens, dOnes) = divmod(j, 10)
        if nTens != dTens:
            if dOnes != 0 and nOnes == dTens and (1.0 * nTens / dOnes) == (1.0 * i / j):
                match = True
            if dTens != 0 and nTens == dOnes and (1.0 * nOnes / dTens) == (1.0 * i / j):
                match = True
        if match:
            print str(i) + "/" + str(j) + " : " + str(1.0 * nTens / dOnes) + " = " + str(1.0 * i / j)
            nResult *= i
            dResult *= j
print nResult, "/", dResult

t.stop()
print t