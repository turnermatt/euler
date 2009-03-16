'''
Created on Mar 15, 2009

@author: mturner
'''
import util

def is_abundant(n):
    return util.sum_of_proper_divisors(n) > n

t = util.Timer()
t.start()

sieve = [i for i in range(28124)]
abundants = []

for n in range(2,28124):
    if n%100 == 0:
        print n
    if is_abundant(n):
        abundants.append(n)

#print "abundants: ", abundants
#for i in range(len(abundants)):
#    print i
#    n = abundants[i]            
#    for m in abundants[i:]:
#        s = m + n
#        if s < 28124 and s in sieve:
#            sieve.remove(s)

#for s in sieve:
#    print s
#    for a in abundants:
#        if s - a in abundants:
#            sieve.remove(s)

abundant_count = len(abundants)
abundant_sums = []
for i in range(len(abundants)):
    if i%100==0:
        print i, "/", abundant_count 
    for x in abundants[i:]:
        if abundants[i] + x < 28124:
            abundant_sums.append(abundants[i] + x)
        else:
            break # stop checking since abundants are sorted so rest are too large

abundant_sums = set(abundant_sums)     

print sum(filter(lambda x: x not in abundant_sums, sieve))
            
#print sum(sieve )

t.stop()
print t