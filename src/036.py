'''
Created on Apr 30, 2009

@author: mturner

The decimal number, 585 = 1001001001_(2) (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''
import util

def is_palindrome(text):
    return text == "".join([c for c in text[::-1]])

def to_bin_str(n):
    out = ''
    while n:
        out = str(n&1) + out
        n = n >> 1
    return out

t = util.Timer()
t.start()

sum = 0
for i in range(1000000):
    if is_palindrome(str(i)) and is_palindrome(to_bin_str(i)):
        sum += i
        print i

print "_____________"
print sum

t.stop()
print t
