'''
Created on Mar 11, 2009

@author: mturner
'''
from time import clock

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
    n += 1
        
finish = clock()
print primes[len(primes)-1]
print "Took ", finish - start, " seconds"