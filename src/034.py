'''
Created on Apr 4, 2009

@author: mturner
'''
import util

t = util.Timer()
t.start()

def factorial(x):
    if x==0: return 1
    if x==1: return 1
    if x==2: return 2
    return x*factorial(x-1)
f = [factorial(x) for x in range(0,10)]

max = sum(f)
result = 0

for x in range(3,max+1):
    if sum([f[int(i)] for i in str(x) ]) == x:
        print x
        result += x
        
print "result:", result



t.stop()
print t