
About the re module
[back to top]

The purpose of this IPython notebook is not to rewrite a detailed tutorial about regular expressions or the in-built Python re module, but to collect some useful regular expressions for copy&paste purposes.

The complete documentation of the Python re module can be found here https://docs.python.org/3.4/howto/regex.html. Below, I just want to list the most important methods for convenience:

re.match() : Determine if the RE matches at the beginning of the string.
re.search() : Scan through a string, looking for any location where this RE matches.
re.findall() : Find all substrings where the RE matches, and returns them as a list.
re.finditer() : Find all substrings where the RE matches, and returns them as an iterator.
If you are using the same regular expression multiple times, it is recommended to compile it for improved performance.

compiled_re = re.compile(r'some_regexpr')    
for word in text:
    match = comp.search(compiled_re))
    # do something with the match
E.g., if we want to check if a string ends with a substring:

In [3]:
import re

needle = 'needlers'

# Python approach
print(bool(any([needle.endswith(e) for e in ('ly', 'ed', 'ing', 'ers')])))

# On-the-fly Regular expression in Python
print(bool(re.search(r'(?:ly|ed|ing|ers)$', needle)))

# Compiled Regular expression in Python
comp = re.compile(r'(?:ly|ed|ing|ers)$') 
print(bool(comp.search(needle)))
True
True
True

In [4]:
%timeit -n 10000 -r 50 bool(any([needle.endswith(e) for e in ('ly', 'ed', 'ing', 'ers')]))
%timeit -n 10000 -r 50 bool(re.search(r'(?:ly|ed|ing|ers)$', needle))
%timeit -n 10000 -r 50 bool(comp.search(needle))
10000 loops, best of 50: 2.74 µs per loop
10000 loops, best of 50: 2.93 µs per loop
10000 loops, best of 50: 1.28 µs per loop




Identify files via file extensions
[back to top]

A regular expression to check for file extensions.

Note: This approach is not recommended for thorough limitation of file types (parse the file header instead). However, this regex is still a useful alternative to e.g., a Python's endswith approach for quick pre-filtering for certain files of interest.

In [5]:
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



Username validation
[back to top]

Checking for a valid user name that has a certain minimum and maximum length.

Allowed characters:

letters (upper- and lower-case)
numbers
dashes
underscores
In [6]:
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



Checking for valid email addresses
[back to top]

A regular expression that captures most email addresses.

In [7]:
pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

str_true = ('test@mail.com',)
            
str_false = ('testmail.com', '@testmail.com', 'test@mailcom')

for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f
source: http://stackoverflow.com/questions/201323/using-a-regular-expression-to-validate-an-email-address



Check for a valid URL
[back to top]

Checks for an URL if a string ...

starts with https://, or http://, or www.
or ends with a dot extension
In [8]:
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
source: http://code.tutsplus.com/tutorials/8-regular-expressions-you-should-know--net-6149



Checking for numbers
[back to top]

Positive integers
In [9]:
pattern = '^\d+$'

str_true = ('123', '1', )
            
str_false = ('abc', '1.1', )

for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f
Negative integers
In [10]:
pattern = '^-\d+$'

str_true = ('-123', '-1', )
            
str_false = ('123', '-abc', '-1.1', )

for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f
All integers
In [11]:
pattern = '^-{0,1}\d+$'

str_true = ('-123', '-1', '1', '123',)
            
str_false = ('123.0', '-abc', '-1.1', )

for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f
Positive numbers
In [12]:
pattern = '^\d*\.{0,1}\d+$'

str_true = ('1', '123', '1.234', )
            
str_false = ('-abc', '-123', '-123.0')

for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f
Negative numbers
In [13]:
pattern = '^-\d*\.{0,1}\d+$'

str_true = ('-1', '-123', '-123.0', )
            
str_false = ('-abc', '1', '123', '1.234', )

for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f
All numbers
In [14]:
pattern = '^-{0,1}\d*\.{0,1}\d+$'

str_true = ('1', '123', '1.234', '-123', '-123.0')
            
str_false = ('-abc')

for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f
source: http://stackoverflow.com/questions/1449817/what-are-some-of-the-most-useful-regular-expressions-for-programmers



Validating dates
[back to top]

Validates dates in mm/dd/yyyy format.

In [15]:
pattern = '^(0[1-9]|1[0-2])\/(0[1-9]|1\d|2\d|3[01])\/(19|20)\d{2}$'

str_true = ('01/08/2014', '12/30/2014', )
            
str_false = ('22/08/2014', '-123', '1/8/2014', '1/08/2014', '01/8/2014')

for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f



[back to top]

12-Hour format
In [29]:
pattern = r'^(1[012]|[1-9]):[0-5][0-9](\s)?(?i)(am|pm)$'

str_true = ('2:00pm', '7:30 AM', '12:05 am', )
            
str_false = ('22:00pm', '14:00', '3:12', '03:12pm', )

for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f
24-Hour format
In [18]:
pattern = r'^([0-1]{1}[0-9]{1}|20|21|22|23):[0-5]{1}[0-9]{1}$'

str_true = ('14:00', '00:30', )
            
str_false = ('22:00pm', '4:00', )

for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f



Checking for HTML tags
[back to top]

Also this regex is only recommended for "filtering" purposes and not a ultimate way to parse HTML. For more information see this excellent discussion on StackOverflow:
http://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags/

In [16]:
pattern = r"""</?\w+((\s+\w+(\s*=\s*(?:".*?"|'.*?'|[^'">\s]+))?)+\s*|\s*)/?>"""

str_true = ('<a>', '<a href="something">', '</a>', '<img src>')
            
str_false = ('a>', '<a ', '< a >')

for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f
source: http://haacked.com/archive/2004/10/25/usingregularexpressionstomatchhtml.aspx/



Checking for IP addresses
[back to top]

IPv4


Image source: http://en.wikipedia.org/wiki/File:Ipv4_address.svg
In [8]:
pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

str_true = ('172.16.254.1', '1.2.3.4', '01.102.103.104', )
            
str_false = ('17216.254.1', '1.2.3.4.5', '01 .102.103.104', )

for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f
source: http://answers.oreilly.com/topic/318-how-to-match-ipv4-addresses-with-regular-expressions/
Ipv6


Image source: http://upload.wikimedia.org/wikipedia/commons/1/15/Ipv6_address.svg
In [21]:
pattern = r'^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$'

str_true = ('2001:470:9b36:1::2',
            '2001:cdba:0000:0000:0000:0000:3257:9652', 
            '2001:cdba:0:0:0:0:3257:9652', 
            '2001:cdba::3257:9652', )
            
str_false = ('1200::AB00:1234::2552:7777:1313', # uses `::` twice
             '1200:0000:AB00:1234:O000:2552:7777:1313', ) # contains an O instead of 0

for t in str_true:
    assert(bool(re.match(pattern, t)) == True), '%s is not True' %t
for f in str_false:
    assert(bool(re.match(pattern, f)) == False), '%s is not False' %f
source: http://snipplr.com/view/43003/regex--match-ipv6-address/



Checking for MAC addresses
[back to top]



Image source: http://upload.wikimedia.org/wikipedia/en/3/37/MACaddressV3.png
In [29]:
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
