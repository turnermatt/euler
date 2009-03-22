'''
Created on Mar 16, 2009

@author: mturner
'''
import util

def swap(v, i, j):
    t = v[i]
    v[i] = v[j]
    v[j] = t
    return v

def rotateLeft(v, start):
    tmp = v[start]
    for i in range(start,len(v)-1):
        v[i] = v[i+1]
    v[len(v)-1] = tmp
    return v
    
def permute(v, start=0):
    n = len(v)
    global count
    count += 1
    if count == 1000000:
        print v
    if start < n:
        for i in range(n-2, start-1, -1):
            for j in range(i+1,n):
                swap(v,i,j)
                permute(v,i+1)
            rotateLeft(v, i)
            

t = util.Timer()
t.start()

count = 0
permute([x for x in range(0,10)])

t.stop()
print t