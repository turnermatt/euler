'''
Created on Mar 11, 2009

@author: mturner
'''
import util

class TriangleNumber():
    
    def __getitem__(self,n):
#        return sum(range(n+1))
        return (n**2 + n)/2
        
        
def get_divisors(n):
    factors = []
    for i in range(1,int(n/2)+1):
        if n%i == 0:
            factors.append(i)
    factors.append(n)
    return factors

def divisor_sigma_0(n):
    remain = n
    result = 1
    primes = util.primes_upto(int(n/2+1))
    i=0
    curr_mult = 0 # multiplicity of the current prime
    while i < len(primes):
        curr_prime = primes[i]
        if remain%curr_prime==0:
            remain = remain/curr_prime
            curr_mult += 1
        else:
            if curr_mult > 0:
                result *= curr_mult + 1
                curr_mult = 0
            i += 1
    return result==1 and n!=1 and 2 or result
                
def brute_sigma(n):
    result = 0
    sqrt = n**.5
    for i in range(1, int(sqrt + 1)):
        if n%i == 0:
            result += 2
    if sqrt == int(sqrt):
        result -= 1    
    return result 

t = util.Timer()
t.start()

#tn = TriangleNumber()
#k = 0
#while True:
#    if k%10 == 0:
#        print k
#    if divisor_sigma_0(tn[k]) > 500:
#        print k, tn[k]
#        break
#    k += 1

#for k in range(61,71):
#    print k, divisor_sigma_0(k), brute_sigma(k)

k=0
while True:
    if k%1==0:
        print k, (k**2+k)/2, brute_sigma((k**2+k)/2)
    if brute_sigma((k**2+k)/2) > 500:
        print k,TriangleNumber()[k], brute_sigma((k**2+k)/2)
        print get_divisors(TriangleNumber()[k])
        break
    k += 1 

t.stop()
print t