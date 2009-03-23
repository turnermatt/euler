'''
Created on Mar 22, 2009

@author: mturner
'''
import util

t = util.Timer()
t.start()

# take a guess that n won't be larger than 200
# so...generate primes less than 200**2 + 1000*200 + 1000
n_max_guess = 200
val_max_guess = n_max_guess**2 + 1000*n_max_guess + 1000
primes = util.primes_upto(val_max_guess)
print "Found " + str(len(primes)) + " prime numbers."
primes_table = [False for x in range(val_max_guess)]
for i in primes:
    primes_table[i] = True
print "Finished constructing primes table"

max_pair = (0,0)
max_n = 0
for a in range(-999,1000):
    for b in range(-999,1000):
        n = 0
        while True:
            val = n**2 + a*n + b
            if val > val_max_guess:
                print "n_max_guess too small."
                break
            elif primes_table[val]:
                if n > max_n:
                    max_n = n
                    max_pair = (a,b)
                    print "New max", max_n, "at", max_pair
                n += 1
            else:
                break

print max_pair[0]*max_pair[1]
print 70**2 - 70*61 + 971

#valid_pairs = [primes_table[max_n**2 + max_n*a + b] and (a,b) for a in range(-999,1000) for b in range(-999,1000)]
#print "Found", len(valid_pairs), "valid pairs at n =", max_n
#
#print max_pair[0]*max_pair[1]


t.stop()
print t