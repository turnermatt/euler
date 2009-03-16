'''
Created on Mar 16, 2009

@author: mturner
'''
import util

t = util.Timer()
t.start()

x=1
y=1
z=2
idx = 3
while (len(str(z)) < 1000):
    x = y
    y = z
    z = x + y
    idx += 1
    if idx%100 == 0: print idx
    
print idx

t.stop()
print t