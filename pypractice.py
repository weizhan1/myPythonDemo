grep -l -R --perl-regexp "\b(\(\d{3}\)\s*|\d{3}-)\d{3}-\d{4}\b" * > output.txt

# coding: utf-8

# In[1]:

import re

needle = 'needlers'

# Python approach
print(bool(any([needle.endswith(e) for e in ('ly', 'ed', 'ing', 'ers')])))

# On-the-fly Regular expression in Python
print(bool(re.search(r'(?:ly|ed|ing|ers)$', needle)))

# Compiled Regular expression in Python
comp = re.compile(r'(?:ly|ed|ing|ers)$') 
print(bool(comp.search(needle)))


# In[2]:

get_ipython().magic("timeit -n 10000 -r 50 bool(any([needle.endswith(e) for e in ('ly', 'ed', 'ing', 'ers')]))")
get_ipython().magic("timeit -n 10000 -r 50 bool(re.search(r'(?:ly|ed|ing|ers)$', needle))")
get_ipython().magic('timeit -n 10000 -r 50 bool(comp.search(needle))')


# In[3]:

pattern = r'(?i)(\w+)\.(jpeg|jpg|png|gif|tif|svg)$'

# remove `(?i)` to make regexpr case-sensitive

str_true = ('test.gif', 
            'image.jpeg', 
            'image.jpg',
            'image.TIF'
            )

str_false = ('test.pdf',
             'test.gif.pdf',
             )

for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f


# In[4]:

min_len = 5 # minimum length for a valid username
max_len = 15 # maximum length for a valid username

pattern = r"^(?i)[a-z0-9_-]{%s,%s}$" %(min_len, max_len)

# remove `(?i)` to only allow lower-case letters



str_true = ('user123', '123_user', 'Username')
            
str_false = ('user', 'username1234_is-way-too-long', 'user$34354')

for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f


# In[5]:

pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
str_true = ('test@mail.com',)
str_false = ('testmail.com', '@testmail.com', 'test@gmail.com')
for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f


# In[6]:

pattern = '^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$'
str_true = ('https://github.com', 
            'http://github.com',
            'www.github.com',
            'github.com',
            'test.de',
            'https://github.com/rasbt',
            'test.jpeg' # !!! 
            )
            
str_false = ('testmailcom', 'http:testmailcom', )

for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f


# In[7]:

pattern = '^\d+$'

str_true = ('123', '1', )
            
str_false = ('abc', '1.1', )

for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f


# In[8]:

pattern = '^-\d+$'

str_true = ('-123', '-1', )
            
str_false = ('123', '-abc', '-1.1', )

for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f


# In[9]:

pattern = '^-{0,1}\d*\.{0,1}\d+$'

str_true = ('1', '123', '1.234', '-123', '-123.0')
            
str_false = ('-abc')

for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f


# In[10]:

pattern = '^(0[1-9]|1[0-2])\/(0[1-9]|1\d|2\d|3[01])\/(19|20)\d{2}$'

str_true = ('01/08/2014', '12/30/2014', )
            
str_false = ('22/08/2014', '-123', '1/8/2014', '1/08/2014', '01/8/2014')

for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f


# In[11]:

pattern = r'^(1[012]|[1-9]):[0-5][0-9](\s)?(?i)(am|pm)$'

str_true = ('2:00pm', '7:30 AM', '12:05 am', )
            
str_false = ('22:00pm', '14:00', '3:12', '03:12pm', )

for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f


# In[12]:

pattern = r'^([0-1]{1}[0-9]{1}|20|21|22|23):[0-5]{1}[0-9]{1}$'

str_true = ('14:00', '00:30', )
            
str_false = ('22:00pm', '4:00', )

for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f


# In[13]:

pattern = r"""</?\w+((\s+\w+(\s*=\s*(?:".*?"|'.*?'|[^'">\s]+))?)+\s*|\s*)/?>"""

str_true = ('<a>', '<a href="something">', '</a>', '<img src>')
            
str_false = ('a>', '<a ', '< a >')

for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f


# In[14]:

pattern = r"""</?\w+((\s+\w+(\s*=\s*(?:".*?"|'.*?'|[^'">\s]+))?)+\s*|\s*)/?>"""

str_true = ('<a>', '<a href="something">', '</a>', '<img src>')
            
str_false = ('a>', '<a ', '< a >')

for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f


# In[15]:

pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

str_true = ('172.16.254.1', '1.2.3.4', '01.102.103.104', )
            
str_false = ('17216.254.1', '1.2.3.4.5', '01 .102.103.104', )

for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f


# In[16]:

pattern = r'^(?i)([0-9A-F]{2}[:-]){5}([0-9A-F]{2})$'

str_true = ('94-AE-70-A0-66-83', 
            '58-f8-1a-00-44-c8',
            '00:A0:C9:14:C8:29'
            , )
            
str_false = ('0:00:00:00:00:00', 
             '94-AE-70-A0 -66-83', ) 

for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f


# In[17]:

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",alist)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)


# In[18]:

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and                alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and                rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)


# In[19]:

range(2,10)


# In[20]:

list(range(2,10))


# In[22]:

def is_prime(num):
    for j in range(2,num):
        if (num % j) == 0:
            return False
    return True
is_prime(2)
is_prime(4)


# In[23]:

list(range(2,2))


# In[25]:

import math
def is_prime(num):
    for j in range(2,int(math.sqrt(num)+1)):
        if (num % j) == 0:
            return False
    return True
is_prime(2)
is_prime(4)


# In[30]:

from collections import deque
def palchecker(aString):
    chardeque = deque()

    for ch in aString:
        chardeque.append(ch)

    stillEqual = True

    while len(chardeque) > 1 and stillEqual:
        first = chardeque.popleft()
        last = chardeque.pop()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))


# In[31]:

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)


# In[33]:

def insertionSort(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position - 1
            
        alist[position] = currentvalue
        
alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)


# In[34]:

def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
print(fib(10))


# In[35]:

def fibR(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fibR(10))


# In[36]:

def memoize(fn, arg):
    memo = {}
    if arg not in memo:
        memo[arg] = fn(arg)
    return memo[arg]

fibm = memoize(fib,10)
print(fibm)


# In[38]:

class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, arg):
        if arg not in self.memo:
            self.memo[arg] = self.fn(arg)
        return self.memo[arg]
@Memoize
def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a
print(fib(10))


# In[45]:

a,b = 0,1
def fibI():
    global a,b
    while True:
        a,b = b,a+b
        yield a
        
f=iter(fibI())
next(f)
print(a, b)
next(f)
print(a, b)
next(f)
print(a, b)
next(f)
print(a, b)


# In[44]:

a = [1, 2, 3, 4]
b = iter(a)
next(b)


# In[46]:

"""
This is the "example" module.
The example module supplies one function, factorial().  For example,
>>> factorial(5)
120
"""

def factorial(n):
    """Return the factorial of n, an exact integer >= 0.
    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000
    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()


# In[49]:

def func():
    print(s)
s = "I hate spam"
func()


# In[50]:

def func():
    s = "Me too."
    print(s)
s = "I hate spam"
func()
print(s)


# In[53]:

def func():
    print(s)
    s = "Me too."
    print(s)

s = "I hate spam." 
func()
print(s)


# In[54]:

def func():
    global s
    print(s)
    s = "That's clear."
    print(s)


s = "Python is great!" 
func()
print(s)


# In[56]:

def func():
    s1 = "I am globally not known"
    print(s1)

func()
print(s1)


# In[58]:

def foo(x, y):
    global a
    a = 42
    x,y = y,x
    b = 33
    b = 17
    c = 100
    print(a,b,x,y)

a,b,x,y = 1,15,3,4
foo(17,4)
print(a,b,x,y)


# In[59]:

def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                
alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)

def shortBubbleSort(alist):
    exchange = True
    passnum = len(alist)-1
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                exchange = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum - 1
        
alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)
                
            
            


# In[60]:

def anagramSolution(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)
    alist1.sort()
    alist2.sort()
    
    pos = 0 
    matches = True
    
    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos+1
        else:
            matches = False
    return matches

print (anagramSolution('abcde', 'ecbda'))


# In[61]:

def anagramSolution2(s1, s2):
    c1 = [0]*26
    c2 = [0]*26
    
    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos]+1
        
    for i in range(len(s2)):
        pos = ord(s1[i])-ord('a')
        c2[pos] = c2[pos]+1
        
    j = 0 
    stillOK = True
    
    while j < 26 and stillOK:
        if c1[j] == c2[j]:
            j = j+1
        else:
            stillOK = False
    return stillOK

print(anagramSolution2('apple', 'pleap'))


# In[62]:

def anagramSolution3(s1, s2):
    alist = list(s2)
    pos1 = 0
    stillOK = True
    
    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2+1
                
        if found:
            alist[pos2] = None
        else:
            stillOK= False
            
        pos1 = pos1+1
        
    return stillOK
    
print(anagramSolution3('abcd','dcba'))


# In[63]:

def binarySearch(alist, item):
2        first = 0
3        last = len(alist)-1
4        found = False
5    
6        while first<=last and not found:
7            midpoint = (first + last)//2
8            if alist[midpoint] == item:
9                found = True
10            else:
11                if item < alist[midpoint]:
12                    last = midpoint-1
13                else:
14                    first = midpoint+1
15    
16        return found
17    
18    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
19    print(binarySearch(testlist, 3))
20    print(binarySearch(testlist, 13))


# In[ ]:

def binarySearch(alist, item):
2        if len(alist) == 0:
3            return False
4        else:
5            midpoint = len(alist)//2
6            if alist[midpoint]==item:
7              return True
8            else:
9              if item<alist[midpoint]:
10                return binarySearch(alist[:midpoint],item)
11              else:
12                return binarySearch(alist[midpoint+1:],item)
13    
14    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
15    print(binarySearch(testlist, 3))
16    print(binarySearch(testlist, 13))

