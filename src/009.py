'''
Created on Mar 11, 2009

@author: mturner
'''
from time import clock

start = clock()


# First try using euclid's formula + brute force
# generate them using m
done = False
for m in range(1000):
    if not done:
        for n in range(m):
            a = 2*m*n
            b = m**2 - n**2
            c = m**2 + n**2
            
            if a**2 + b**2 == c**2 and a+b+c==1000:
                print a*b*c
                done = True
                break
    else:
        break



finish = clock()
print "Took ", finish - start, " seconds."