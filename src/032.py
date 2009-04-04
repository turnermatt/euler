'''
Created on Mar 25, 2009

@author: mturner
'''
import util

t = util.Timer()
t.start()

p = util.Permutations([str(x) for x in range(1,10)])
#p = [[str(x) for x in [3,9,1,8,6,7,2,5,4]]]

products = []
for perm in p:
    for i in range(1,len(perm)-2):
        for j in range(i+1, len(perm)-1):
            a = int("".join(perm[0:i]))
            b = int("".join(perm[i:j]))
            c = int("".join(perm[j:]))
            if a * b > c:
                break
            elif a * b == c:
                products.append(c)
                print a, "*", b, "=", c
                break
print sum(set(products))

t.stop()
print t