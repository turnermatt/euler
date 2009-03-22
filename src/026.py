'''
Created on Mar 22, 2009

@author: mturner
'''
import util

t = util.Timer()
t.start()

def long_divide(d):
    numerator = 1
    denominator = d
    decimal = []
    remainders = {}
    while True:
        numerator *= 10
        (quotient,remain) = divmod(numerator, denominator)
        decimal.append(str(quotient));
        if remain == 0:
            break
        if remain in remainders.values():
            foundCycle = False
            for key,value in remainders.items():
                if quotient == int(decimal[key]) and remain == value:
                    decimal.insert(key,"(")
                    decimal[-1] = ")"
                    foundCycle = True
                    break
            if foundCycle:
                break
        
        remainders[len(decimal)-1] = remain
        numerator = remain        
                    
    return "0." + "".join(decimal)


def unit_fraction_cycle_length(d):
    numerator = 1
    denominator = d
    decimal = []
    remainders = {}
    while True:
        numerator *= 10
        (quotient,remain) = divmod(numerator, denominator)
        decimal.append(str(quotient));
        if remain == 0:
            return 0
        if remain in remainders.values():
            for key,value in remainders.items():
                if quotient == int(decimal[key]) and remain == value:
                    return len(decimal) - key -1            
        remainders[len(decimal)-1] = remain
        numerator = remain      
  

d,max_cycle = 0,0      
for x in range(2,1000):
    cycle_length = unit_fraction_cycle_length(x)
    if cycle_length > max_cycle:
        d = x
        max_cycle = cycle_length
print d
t.stop()
print t