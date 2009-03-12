'''
Created on Mar 12, 2009

@author: mturner
'''
import util

t = util.Timer()
t.start()

known_paths = {}


def move_from(loc):
    (x,y) = loc
    right_count=down_count=0
    if loc == (0,0):
        return 1
    if not loc in known_paths:
        if x != 0:
            right_count = move_from((x-1,y))
        if y != 0:
            down_count = move_from((x,y-1))
        known_paths[loc] = right_count + down_count
    return known_paths[loc]
        
print move_from((20,20))
    


t.stop()
print t