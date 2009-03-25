'''
Created on Mar 25, 2009

@author: mturner
'''
import util

t = util.Timer()
t.start()

# 9**5*6 has six digits, so all answers must have 6 or less digits

total = 0
for i in range(2, 9**5 * 6 + 1):
    sum = 0
    for digit in str(i):
        sum += int(digit)**5
        if sum > i: pass
    if sum == i:
        print i 
        total += sum
    
print "_________"    
print total






t.stop()
print t