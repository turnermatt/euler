'''
Created on Mar 15, 2009

@author: mturner
'''
import util

t = util.Timer()
t.start()

f = reduce(lambda x,y: x*y, range(1,101) )
print sum([int(x) for x in str(f)])

t.stop()
print t