'''
Created on Mar 11, 2009

@author: mturner
'''
from math import sqrt, floor
from time import clock, sleep

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


def get_proper_divisors(n):
    if n < 2: return []
    divisors = [1]
    sqrt = n**.5    
    for i in range(2,int(sqrt + 1)):
        if n%i == 0:
            divisors.extend([i,int(n/i)])
    
    return set(divisors)

def sum_of_divisors(n): # e.g. n = 5
    summ = 1 # don't clobber sum()
    p = 2 
    while p*p <= n and n > 1:
        if n % p == 0: 
            j = p*p 
            n = n/p 
            while n%p == 0: 
                j = j * p 
                n = n/p 
            summ = summ * (j-1) 
            summ = summ / (p-1) 
        if p==2: p = 3
        else: p = p + 2 
    if n > 1: summ = summ * (n+1)
    return summ     
            

def sum_of_proper_divisors(n):
    return sum_of_divisors(n) - n

def primes_upto(n):
    if n <= 2: return []
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
        
        
class Timer:
    
    def start(self):
        self.start_time = clock()
        
    def stop(self):
        self.stop_time = clock()
        
    def __str__(self):
        if (self.start_time==0 or self.stop_time==0):
            return "error"
        diff = self.stop_time - self.start_time
        return "%0.2f seconds" % diff
        
        
if __name__=='__main__':
    for n in range(1000):
        if n%100 == 0: 
            print n
            print n, sum_of_divisors(n) 
    
class Permutations:
    perms = []
    
    def __getitem__(self, n):
        return self.perms[n]
    
    def __len__(self):
        return len(self.perms)
    
    def __init__(self, things):
        self.permute(things)
    
    def swap(self, v, i, j):
        t = v[i]
        v[i] = v[j]
        v[j] = t
        return v
    
    def rotateLeft(self, v, start):
        tmp = v[start]
        for i in range(start,len(v)-1):
            v[i] = v[i+1]
        v[len(v)-1] = tmp
        return v
        
    def permute(self, v, start=0):
        tmp = []
        tmp[:] = v[:]
        self.perms.append(tmp)
        n = len(v)
        if start < n:
            for i in range(n-2, start-1, -1):
                for j in range(i+1,n):
                    self.swap(v,i,j)
                    self.permute(v,i+1)
                self.rotateLeft(v, i)
    
    
      