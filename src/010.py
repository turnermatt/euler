'''
Created on Mar 11, 2009

@author: mturner
'''
from time import clock
import util

start = clock()

print sum(util.primes_upto(2000000))


finish = clock()
print "Took ", finish - start, " seconds."