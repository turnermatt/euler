'''
Created on Jun 2, 2009

@author: mturner
'''

import util

t = util.Timer()
t.start()

MAX_P = 1000

count = [0 for x in range(MAX_P + 1)]

# slow!  but within the 'one minute rule'
for i in range(1,MAX_P):
    print i
    for j in range(i,MAX_P + 1 - i):
#        print "    ",j
        for k in range(j,MAX_P + 1 - i - j):
#            print "        ",k
            if i+j+k <= MAX_P:
                if i**2 + j**2 == k**2:
                    count[i+j+k] = count[i+j+k] + 1
                    print "            ",i,j,k

print '---'
print max(count)
print count[120]
print count.index(max(count))


t.stop()
print t