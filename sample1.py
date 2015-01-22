#! python
from gtk._gtk import ARG_CHILD_ARG

def fib(n):
    # return a fib number
    result = []
    a, b = 0, 1
    while b<n:
        result.append(b)
        a, b = b, a+b 
    return result
# ======================
f100 = fib(100) # call it
print f100

print "Hello, Python"

STRING = "My best friend"
print STRING

x = int(raw_input("Please enter an integer:"))

if x<0:
    x=0
    print 'Negative change to zero'
elif x==0:
    print 'Zero'
elif x==1:
    print 'Single'
else:
    print 'More'
    
a = ['cat', 'window', 'defenestrate']
for x in a:
    print x, len(x)
    
print range(10)

print range(5,10)
print range(0, 10, 3)   

# for n in range(2, 1000):
#     for x in range(2, n):
#         if n % x ==0:
#             print n, 'equals', x, '*', n/x
#             break
#         else:
#             # loop fall through without finding a factor
#             print n, 'is a prime number'

# while True:
#     pass            

word = 'Help' + 'A'
print word

print '<' + word*5 + '>'
str1 = 'str' 'ing'
print str1 

str2='str'.strip() + 'ing'
print str2 

print word[4]
print word[0:2]
print word[2:4]
print word[:2]
print word[2:]

print 'x' + word[1:]
print 'Splat' + word[4]
print word[:2] + word[2:]
print word[2:1]
print word[-1]
print word[-2:]
print word[:-2]

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'): return True
        if ok in ('n', 'no', 'nop', 'nope'): return False
        retries = retries - 1
        if retries < 0: raise IOError, 'refused user'
        print complaint
        
i = 5
def f(arg=i):
    print arg
i = 6
f()

z=ask_ok('really quit???')

if z==False:
    print 'bad'

def make_incrementor(n):
    return lambda x: x+n

f = make_incrementor(42)

print f(0)
print f(1)
print f(15)

import math

print math.cos(math.pi / 4.0)
print math.log(1024, 2)

import random

print random.choice(['apple', 'pear', 'banana'])
print random.sample(xrange(100), 10)
print random.random()

print random.randrange(6)

def perm(l):
    # list of permutations
    if len(l) <= 1:
        return [l]
    r = []
    for i in range(len(l)):
        #print l[:i], l[i+1:]
        s = l[:i] + l[i+1:]
        #print s
        p = perm(s)
        for x in p:
            print l[i:i+1]
            r.append(l[i:i+1] + x)
    return r   

b=[1,2,3]

print perm(b)

# permutation = n! / (n-r)!
# combination = n! / r!(n-r)!

a=2+3j
b=2-3j

# (x+yi)(u+vi) = (xu - yv) + (xv+yu)i

print a*a
print a*b
print a.real
print b.imag

while True:
    try:
        x = int(raw_input("Please enter a number: "))
        break
    except ValueError:
        print "Oops! That was not valid number. Try again .."
            
import string, sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(string.strip(s))
except IOError, (errno, strerror):
    print "Couldn't convert data to an integer."
except ValueError:
    print "Unexpected error:", sys.exc_info()[0]
    raise

