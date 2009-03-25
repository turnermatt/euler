'''
Created on Mar 25, 2009

@author: mturner
'''
import util

t = util.Timer()
t.start()

def count_ways(total, coin_values):
    print "testing", total, coin_values
    if len(coin_values) == 1:
        return total%coin_values[0] == 0 and 1 or 0
    count = 0 
    if coin_values[0] <= total:
        mult = 1
        while coin_values[0] * mult <= total:
            count += count_ways(total - coin_values[0] * mult, coin_values[1:])
            mult += 1
            
    count += count_ways(total, coin_values[1:])
    return count

print count_ways(200, [200,100,50,20,10,5,2,1])
        
    
    


t.stop()
print t