'''
Created on Mar 15, 2009

@author: mturner
'''
import util


t = util.Timer()
t.start()

divisor_sums = [-1 for x in range(10000)]
pair_sum = 0
for i in range(2,10000):
    divisor_sum = sum(util.get_proper_divisors(i))
    if divisor_sum < 10000 and divisor_sums[divisor_sum] == i:
        pair_sum += i
        pair_sum += divisor_sum
        print i,divisor_sum
    divisor_sums[i] = divisor_sum
    
print pair_sum

t.stop()
print t