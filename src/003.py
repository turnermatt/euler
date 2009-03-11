'''
Created on Mar 11, 2009

@author: mturner
'''
import math

steps = 0

def factor(n, minFactor=2):
    global steps 
    print "factoring %d\n" % n
    factors = []
    maxDivisor = int(math.sqrt(n))
    found = False
    for d in range(minFactor,maxDivisor+1):
        steps += 1
        if n % d == 0: 
            factors.append(d)
            factors.extend(factor(int(n/d),d))
            found = True
            break
    if not found: factors.append(n)
    return factors
        
print factor(600851475143)
print "completed in %d steps" % steps


        
        
        