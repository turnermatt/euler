'''
Created on Mar 11, 2009

@author: mturner
'''

def is_palindrome(s):
    if len(s)<2:
        return True
    if s.endswith(s[0:1]):
        return is_palindrome(s[1:-1])
    return False

palindromes = []
for i in range(100,1000):
    for j in range(i+1,1000):
        prod = i*j
        if is_palindrome("%d" % prod):
            palindromes.append(prod)
            
palindromes.sort()
print palindromes[len(palindromes)-1]
        