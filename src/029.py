'''
Created on Mar 25, 2009

@author: mturner
'''
import util

t = util.Timer()
t.start()

print len(set([a**b for a in range(2,101) for b in range(2,101)]))


t.stop()
print t