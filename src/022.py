'''
Created on Mar 15, 2009

@author: mturner
'''
import util

t = util.Timer()
t.start()


names = file('022-names.txt').read().split(",")
names = [name.strip('"') for name in names]
names.sort()
total = 0
pos = 0
for name in names:
    pos += 1
    score = sum([ord(char)-64 for char in name])
    total += pos * score
    
print total

t.stop()
print t