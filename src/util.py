'''
Created on Mar 11, 2009

@author: mturner
'''
from math import sqrt, floor

def is_prime(n):
    if n<=1:
        return False
    if n<4: # 2 & 3 are prime
        return True
    if n%2 == 0:
        return False
    if n<9: # already excluded 4,6,8
        return True
    if n%3 == 0:
        return False
    
    # All primes greater than 3 can be written in the form 6k+/-1
    # So we can start at 5 and increment by 6
    r = floor(sqrt(n))
    f = 5
    while f <= r:
        if n%f == 0 or n%(f+2) == 0: 
            return False
        f += 6
    return True

def primes_upto(n):
    l = range(2,n)
    i = 0
    maxFactor = floor(sqrt(n))
    while l[i]<=maxFactor:
        f = l[i]
        l = [x for x in l if x <= f or not x%f==0]
        i += 1
    return l

class Primes:
    def __getitem__(self, n):
        '''Get the nth prime number (indexed from zero)'''
        if n == 0: return 2     
        limit = n
        idx = 0
        candidate = 1
        while (idx < limit):
            candidate += 2
            if is_prime(candidate):
                idx += 1
        return candidate
        
        
        
if __name__=='__main__':
    print primes_upto(2000000)
    
    
      