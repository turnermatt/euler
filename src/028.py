'''
Created on Mar 25, 2009

@author: mturner
'''
import util

t = util.Timer()
t.start()

spiral_size = 1001

total = 1
mult = 0
prev_term = 1
inc_mult = True
while True:
    if inc_mult: mult += 1
    this_term = prev_term + mult*4
    
    if this_term > spiral_size**2:
        break 
    total += this_term
    prev_term = this_term
    inc_mult = not inc_mult
    print total
    
prev_term = 1
mult = 0
while True:
    mult += 1
    this_term = prev_term + 2 * mult
    if this_term > spiral_size**2:
        break
    total += this_term
    prev_term = this_term
    print total

t.stop()
print t