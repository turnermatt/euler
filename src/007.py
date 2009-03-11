'''
Created on Mar 11, 2009

@author: mturner
'''
from time import clock
import util
import math

start = clock()
primes = [2]

n = 3
while len(primes) < 10001:
    is_prime = True
    for d in primes:
        if n%d == 0:
            is_prime = False
            break
    if is_prime: 
        primes.append(n)
    n += 2
        
finish = clock()
print primes[len(primes)-1]
print "Took ", finish - start, " seconds"

start2 = clock()
limit = 10001
count = 1
candidate = 1
while count < limit:
    candidate += 2
    if util.is_prime(candidate):
        count += 1
        
print candidate

finish2 = clock()
print "Second run took ", finish2 - start2, " seconds"

start3 = clock()
p = util.Primes()
print p[10000]
finish3 = clock()
print "Third run took ", finish3 - start3, " seconds"