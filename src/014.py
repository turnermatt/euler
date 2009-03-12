'''
Created on Mar 12, 2009

@author: mturner
'''
import util

t = util.Timer()
t.start()

chain_lengths = {}
chain_lengths[1] = 1 

def get_chain_length(n):
    def get_next_link_length(x):
        if x%2 == 0:
            return get_chain_length(x/2)
        else:
            return get_chain_length(3*n + 1)
    if not n in chain_lengths:
        chain_lengths[n] = get_next_link_length(n) + 1        
    return chain_lengths[n]
    
max = 0
for n in range(1, 1000001):
    length = get_chain_length(n)
    if length > max:
        max = length
        print "New max for ", n, " (",max,")"


t.stop()
print t