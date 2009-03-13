'''
Created on Mar 13, 2009

@author: mturner
'''
import util

t = util.Timer()
t.start()

counts = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 
          10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:9, 
          20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6,
          1000:11}

def count_letters(n):
    if not n in counts:
        if n >= 100:
            (hunds, remain) = divmod(n, 100)
            return counts[hunds] + (remain == 0 and 7 or 10 + count_letters(remain))
        (tens, remain) = divmod(n, 10)
        return count_letters(tens*10) + count_letters(remain)
    return counts[n]    

print sum([count_letters(n) for n in range(1, 1001)])

t.stop()
print t