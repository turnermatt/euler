'''
Created on Mar 15, 2009

@author: mturner
'''
import util

t = util.Timer()
t.start()

# 0%7 = monday, first day of century = 1/1/1900 + 365 days
first_day = (1 + 365)%7
months = [31,28,31,30,31,30,31,31,30,31,30,31]

day = first_day
count = day%7 == 0 and 1 or 0
for year in range(1901, 2001):
    for month in months:
        day += month
        if month == 28 and year%4 == 0:
            day += 1
        day = day%7
        if day == 0:
            count += 1
print count
        
    

t.stop()
print t