a = ['spam', 'eggs', 100, 1234]
print "list a = ", a
print "a[0]=", a[0]
print "a[-2]", a[-2]
print "a[1:-1]=", a[1:-1]
print a[:2] + ['bacon', 2*2]
print 3*a[:3] + ['Boe!']
a[2] = a[2] + 23
a[0:2] = [1, 12]
print a
a[0:2] = [] 
print a 
a[1:1] = ['bleach', 'xyzzy']
print a 
a[:0] = []
print a
print "length=", len(a)

q = [2, 3]
p = [1, q, 4]
print p

print len(p)

print p[1], p[1][0]
p[1].append('xtra')
print p
print q


a = [66.6, 333, 333, 1, 1234.5]
print a.count(333), a.count(66.6)

a.insert(2, -1)
print a

a.append(333)
print a

print a.index(333)

a.remove(333)
print a

a.reverse()
print a

a.sort()
print a 

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print stack

x=stack.pop()
print x
print stack
 
x=stack.pop()
print x

queue = ["eric", "john", "michael"]
queue.append("terry")
queue.append("graham")
print queue

s=queue.pop(0)
print s

s=queue.pop(0)
print s
print queue


a = [-1, 1, 66.6, 333, 333, 1234.5]
del a[0]
print a

del a[2:4]
print a

#filter of sequence

def f(x): return x % 2 != 0 and x % 3 != 0

res=filter(f, range(2, 15))

print res


def cube(x): return x*x*x

res=map(cube, range(1, 11))

print res

def add(x,y): return x+y

r=reduce(add, range(1,11))
print r

t = 12345, 65332, 'hello'
print t[0]

print t 

u = t, (1, 2, 3, 4, 5)
print u

tel = {'jack': 4098, 'sape': 4130}
tel['guido'] = 4127
print tel

print tel['jack']

del tel['sape']

tel['irv'] = 4199

print tel

print tel.keys()

x=tel.has_key('guido')
print x

d=dict([('sape', 4139), ('guido', 5168), ('jack', 4335)])
print d

vec=[1,2,3,4,5]
dd=dict([(x, x**2) for x in vec])
print dd

 
