'''
Created on Mar 11, 2009

@author: mturner
'''
import util

t = util.Timer()
#t.start()
#print sum(util.primes_upto(2000000))
#t.stop()
#print t
#
#
#t.start()
#print sum([x for x in range(2000000) if util.is_prime(x)])
#t.stop()
#print t

t.start()
limit = 2000000
sum = 5
n = 5
while n <= limit:
    if util.is_prime(n):
        sum += n
    n += 2
    if n <= limit and util.is_prime(n):
        sum += n
    n += 4    
t.stop()
print t