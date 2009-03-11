'''
Created on Mar 11, 2009

@author: mturner
'''
total = 0
a,b = 0,1
while b <= 4000000:
    if b % 2 == 0: total += b
    a,b = b,a+b
print total

#def fib(n):
#    if n==1:
#        return 1
#    elif n==2:
#        return 2
#    elif n==3:
#        return 3
#    else:
#        return fib(n-1) + fib(n-2)
#    
#print "\n".join(["%d" % fib(x) for x in range(1,15)])