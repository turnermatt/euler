'''
Created on Apr 4, 2009

@author: mturner
'''
import util

t = util.Timer()
t.start()

print sum([x**x for x in range(1,1001)])%10**10


t.stop()
print t