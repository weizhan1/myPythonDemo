import sys

print sys.path

print sys.version
print sys.platform

print sys.maxint

print dir(sys)

print repr(0.1 * 5)
print str("test only")

print repr((3, 5, ('spam', 'egg')))
print `4, 6, ('spam', 'egg')`

hello = 'hello, world\n'
hellos = repr(hello)
print hellos

for x in range(1, 11):
    print repr(x).rjust(2), repr(x*x).rjust(3)
    print repr(x*x*x).rjust(4)
    
    
for x in range(1,11):
    print '%2d %3d %4d' % (x, x*x, x*x*x)

import sys    
print sys.argv

import re

r=re.findall(r'\bf[a-z]*','which foot or hand fell fastest')
print r 

s=re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print s 

import datetime
from datetime import date

now = date.today()
print now

#datetime.date(2003, 12, 2)

print now.strftime("%m-%d-%y or %d%b %Y is a %A on the %d day of %B")

birthday = date(1964, 7, 31)
age = now - birthday
print age.days


    
    
