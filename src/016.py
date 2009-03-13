'''
Created on Mar 13, 2009

@author: mturner
'''
import util

t = util.Timer()
t.start()

#for i in range(1001):
    
x = 2**1000
result = 0
while x>0:
    x, remain = divmod(x, 10)
    result += remain
print result

t.stop()
print t