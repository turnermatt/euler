'''
Created on Mar 11, 2009

@author: mturner
'''

top = 100
print sum([x for x in range(1,top + 1)])**2 - sum([x**2 for x in range(1, top+1)])