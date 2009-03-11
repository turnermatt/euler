'''
Created on Mar 11, 2009

@author: mturner
'''

# brute force
def is_the_one(n, maxFactor):
    for d in range(maxFactor, 1, -1):
        if n % d != 0: return False
    return True

n=20
f=n
while not is_the_one(n, f):
    n += f
print n

    
        