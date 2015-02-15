In [1]:
def _stacktraces():
   code = []
   for threadId, stack in sys._current_frames().items():
       code.append("\n# ThreadID: %s" % threadId)
       for filename, lineno, name, line in traceback.extract_stack(stack):
           code.append('File: "%s", line %d, in %s' % (filename,
                   lineno, name))
           if line:
               code.append("  %s" % (line.strip()))

   for line in code:
       print >> sys.stderr, line
In [ ]:
def worker():
    while True:
        item = q.get()
        do_work(item)
        q.task_done()

q = Queue()
for i in range(num_worker_threads):
     t = Thread(target=worker)
     t.daemon = True
     t.start()

for item in source():
    q.put(item)

q.join()       # block until all tasks are done
In [ ]:
import os
import sys
import time
import signal
import threading
import atexit
import Queue
import traceback 

FILE = '/tmp/dump-stack-traces.txt'

_interval = 1.0

_running = False
_queue = Queue.Queue()
_lock = threading.Lock()

def _stacktraces(): 
    code = [] 
    for threadId, stack in sys._current_frames().items(): 
        code.append("\n# ProcessId: %s" % os.getpid()) 
        code.append("# ThreadID: %s" % threadId) 
        for filename, lineno, name, line in traceback.extract_stack(stack): 
            code.append('File: "%s", line %d, in %s' % (filename, 
                    lineno, name)) 
            if line: 
                code.append("  %s" % (line.strip())) 

    for line in code:
        print >> sys.stderr, line

try:
    mtime = os.path.getmtime(FILE)
except:
    mtime = None

def _monitor():
    while 1:
        global mtime

        try:
            current = os.path.getmtime(FILE)
        except:
            current = None

        if current != mtime:
            mtime = current
            _stacktraces()

        # Go to sleep for specified interval.

        try:
            return _queue.get(timeout=_interval)
        except:
            pass

_thread = threading.Thread(target=_monitor)
_thread.setDaemon(True)

def _exiting():
    try:
        _queue.put(True)
    except:
        pass
    _thread.join()

atexit.register(_exiting)

def _start(interval=1.0):
    global _interval
    if interval < _interval:
        _interval = interval

    global _running
    _lock.acquire()
    if not _running:
        prefix = 'monitor (pid=%d):' % os.getpid()
        print >> sys.stderr, '%s Starting stack trace monitor.' % prefix
        _running = True
        _thread.start()
    _lock.release()

_start()
In [ ]:
def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            yield line

def grep(pattern, lines):
    return (line for line in lines if pattern in lines)

def printlines(lines):
    for line in lines:
        print line,

def main(pattern, filenames):
    lines = readfiles(filenames)
    lines = grep(pattern, lines)
    printlines(lines)
In [3]:
def foo():
    print("begin")
    for i in range(4):
        print("before yield", i)
        yield i
        print("after yield", i)
    print("end")
    
f = foo()
next(f)
begin
before yield 0
Out[3]:
0
In [4]:
next(f)
after yield 0
before yield 1
Out[4]:
1
In [7]:
import collections 

class OrderedClass(type):

     @classmethod
     def __prepare__(metacls, name, bases, **kwds):
        return collections.OrderedDict()

     def __new__(cls, name, bases, namespace, **kwds):
        result = type.__new__(cls, name, bases, dict(namespace))
        result.members = tuple(namespace)
        return result
 
class A(metaclass=OrderedClass):
    def one(self): pass
    def two(self): pass
    def three(self): pass
    def four(self): pass

A.members
Out[7]:
('__module__', '__qualname__', 'one', 'two', 'three', 'four')
In [10]:
class OnlyOne(object):
    class __OnlyOne:
        def __init__(self):
            self.val = None
        def __str__(self):
            return 'self' + self.val
    instance = None
    def __new__(cls): # __new__ always a classmethod
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne()
        return OnlyOne.instance
    def __getattr__(self, name):
        return getatr(self.instance, name)
    def __setattr__(self, name):
        return setattr(self.instance, name)

x = OnlyOne()
x.val = 'sausage'
print(x)
selfsausage
In [11]:
y = OnlyOne()
y.val = 'eggs'
In [12]:
z = OnlyOne()
z.val = 'spam'
In [14]:
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    s1=Singleton()
    s2=Singleton()
    if(id(s1)==id(s2)):
        print("Same")
    else:
        print("Different")
Same
In [ ]:
"""
A generic factory implementation.
Examples:
>>f=Factory()
>>class A:pass
>>f.register("createA",A)
>>f.createA()
<__main__.A instance at 01491E7C>

>>> class B:
... 	def __init__(self, a,b=1):
... 		self.a=a
... 		self.b=b
... 		
>>> f.register("createB",B,1,b=2)
>>> f.createB()
>>> b=f.createB()
>>> 
>>> b.a
1
>>> b.b
2

>>> class C:
... 	def __init__(self,a,b,c=1,d=2):
... 		self.values = (a,b,c,d)
... 
>>> f.register("createC",C,1,c=3)
>>> c=f.createC(2,d=4)
>>> c.values
(1, 2, 3, 4)

>>> f.register("importSerialization",__import__,"cPickle")
>>> pickle=f.importSerialization()
>>> pickle
<module 'cPickle' (built-in)>
>>> f.register("importSerialization",__import__,"marshal")
>>> pickle=f.importSerialization()
>>> pickle
<module 'marshal' (built-in)>

>>> f.unregister("importSerialization")
>>> f.importSerialization()
Traceback (most recent call last):
  File "<interactive input>", line 1, in ?
AttributeError: Factory instance has no attribute 'importSerialization'
"""

class Factory:      
    def register(self, methodName, constructor, *args, **kargs):
        """register a constructor"""
        _args = [constructor]
        _args.extend(args)
        setattr(self, methodName,apply(Functor,_args, kargs))
        
    def unregister(self, methodName):
        """unregister a constructor"""
        delattr(self, methodName)

class Functor:
    def __init__(self, function, *args, **kargs):
        assert callable(function), "function should be a callable obj"
        self._function = function
        self._args = args
        self._kargs = kargs
        
    def __call__(self, *args, **kargs):
        """call function"""
        _args = list(self._args)
        _args.extend(args)
        _kargs = self._kargs.copy()
        _kargs.update(kargs)
        return apply(self._function,_args,_kargs)
In [19]:
class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")
    
c = C()
c.x = 15
c.x
Out[19]:
15
In [23]:
C.x.__doc__
Out[23]:
"I'm the 'x' property."
In [25]:
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
In [27]:
class autoprop(type):
        def __init__(cls, name, bases, dict):
            super(autoprop, cls).__init__(name, bases, dict)
            props = {}
            for name in dict.keys():
                if name.startswith("_get_") or name.startswith("_set_"):
                    props[name[5:]] = 1
            for name in props.keys():
                fget = getattr(cls, "_get_%s" % name, None)
                fset = getattr(cls, "_set_%s" % name, None)
                setattr(cls, name, property(fget, fset))
                
class autosuper(type):
        def __init__(cls, name, bases, dict):
            super(autosuper, cls).__init__(name, bases, dict)
            setattr(cls, "_%s__super" % name, super(cls))
            
            
class autosuprop(autosuper, autoprop):
        pass
            
class A:
        __metaclass__ = autosuprop
        def _get_x(self):
            return "A"
class B(A):
        def _get_x(self):
            return "B" + self.__super._get_x()
class C(A):
        def _get_x(self):
            return "C" + self.__super._get_x()
class D(C, B):
        def _get_x(self):
            return "D" + self.__super._get_x()

assert D().x == "DCBA"
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-27-d8eb5f78140f> in <module>()
     34             return "D" + self.__super._get_x()
     35 
---> 36 assert D().x == "DCBA"

AttributeError: 'D' object has no attribute 'x'
In [ ]:
Implementing __getitem__ in a class allows its instances to use the [] (indexer) operators.

class Test(object):
    def __getitem__(self, items):
        print '%-15s  %s' % (type(items), items)

t = Test()
t[1]
t['hello world']
t[1, 'b', 3.0]
t[5:200:10]
t['a':'z':3]
t[object()]
In [ ]:
class Test(object):
    def __call__(self, *args, **kwargs):
        print args
        print kwargs
        print '-'*80

t = Test()
t(1, 2, 3)
t(a=1, b=2, c=3)
t(4, 5, 6, d=4, e=5, f=6)
In [ ]:
class Test(object):
    def __init__(self):
        self.a = 'a'
        self.b = 'b'

    def __getattr__(self, name):
        return 123456

t = Test()
print 'object variables: %r' % t.__dict__.keys()
print t.a
print t.b
print t.c
print getattr(t, 'd')
print hasattr(t, 'x')
In [ ]:
class Test(object):
    def __init__(self):
        self.a = 'a'
        self.b = 'b'

    def __setattr__(self, name, value):
        print 'set %s to %s' % (name, repr(value))

        if name in ('a', 'b'):
            object.__setattr__(self, name, value)

t = Test()
t.c = 'z'
setattr(t, 'd', '888')
In [28]:
from Tkinter import *

root = Tk()
root.title('A Tkinter Example')

frame = Frame()
frame.pack()

Button(frame, text='One').pack(side=TOP, pady=5)
Button(frame, text='Two').pack(side=TOP, pady=5)
Button(frame, text='Three').pack(side=TOP, pady=5)

frame2 = Frame(frame)
frame2.pack(side=TOP, pady=5)

Button(frame2, text='Apple').pack(padx=5, side=LEFT)
Button(frame2, text='Banana').pack(padx=5, side=LEFT)
Button(frame2, text='Cranberry').pack(padx=5, side=LEFT)

Button(frame, text='Durian').pack(pady=5, side=BOTTOM)

root.mainloop()

frame = VFrame [
    Button(text='One'),
    Button(text='Two'),
    Button(text='Tree'),

    HFrame [
        Button(text='Apple'),
        Button(text='Banana'),
        Button(text='Cranberry'),
    ],

    Button(text='Durian')
]

frame.show('A Cool Tkinter Example')
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
<ipython-input-28-c37951d5a796> in <module>()
----> 1 from Tkinter import *
      2 
      3 root = Tk()
      4 root.title('A Tkinter Example')
      5 

ImportError: No module named 'Tkinter'
In [ ]:
class SimpleMeta1(type):
    def __init__(cls, name, bases, nmspc):
        super(SimpleMeta1, cls).__init__(name, bases, nmspc)
        cls.uses_metaclass = lambda self : "Yes!"

class Simple1(object):
    __metaclass__ = SimpleMeta1
    def foo(self): pass
    @staticmethod
    def bar(): pass

simple = Simple1()
print([m for m in dir(simple) if not m.startswith('__')])
# A new method has been injected by the metaclass:
print simple.uses_metaclass()
In [ ]:
class Simple2(object):
    class __metaclass__(type):
        def __init__(cls, name, bases, nmspc):
            # This won't work:
            # super(__metaclass__, cls).__init__(name, bases, nmspc)
            # Less-flexible specific call:
            type.__init__(cls, name, bases, nmspc)
            cls.uses_metaclass = lambda self : "Yes!"

class Simple3(Simple2): pass
simple = Simple3()
print simple.uses_metaclass()
In [ ]:
class Simple4(object):
    def __metaclass__(name, bases, nmspc):
        cls = type(name, bases, nmspc)
        cls.uses_metaclass = lambda self : "Yes!"
        return cls

simple = Simple4()
print simple.uses_metaclass()
In [ ]:
class final(type):
    def __init__(cls, name, bases, namespace):
        super(final, cls).__init__(name, bases, namespace)
        for klass in bases:
            if isinstance(klass, final):
                raise TypeError(str(klass.__name__) + " is final")

class A(object):
    pass

class B(A):
    __metaclass__= final

print B.__bases__
print isinstance(B, final)

# Produces compile-time error:
class C(B):
    pass
In [29]:
class Singleton(type):
    instance = None
    def __call__(cls, *args, **kw):
        if not cls.instance:
             cls.instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.instance

class ASingleton(object):
    __metaclass__ = Singleton

a = ASingleton()
b = ASingleton()
assert a is b
print(a.__class__.__name__, b.__class__.__name__)

class BSingleton(object):
    __metaclass__ = Singleton

c = BSingleton()
d = BSingleton()
assert c is d
print(c.__class__.__name__, d.__class__.__name__)
assert c is not a
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-29-2d76e19fba70> in <module>()
     11 a = ASingleton()
     12 b = ASingleton()
---> 13 assert a is b
     14 print(a.__class__.__name__, b.__class__.__name__)
     15 

AssertionError: 
In [ ]:
def singleton(klass):
    "Simple replacement of object creation operation"
    def getinstance(*args, **kw):
        if not hasattr(klass, 'instance'):
            klass.instance = klass(*args, **kw)
        return klass.instance
    return getinstance

def singleton(klass):
    """
    More powerful approach: Change the behavior
    of the instances AND the class object.
    """
    class Decorated(klass):
        def __init__(self, *args, **kwargs):
            if hasattr(klass, '__init__'):
                klass.__init__(self, *args, **kwargs)
        def __repr__(self) : return klass.__name__ + " obj"
        __str__ = __repr__
    Decorated.__name__ = klass.__name__
    class ClassObject:
        def __init__(cls):
            cls.instance = None
        def __repr__(cls):
            return klass.__name__
        __str__ = __repr__
        def __call__(cls, *args, **kwargs):
            print str(cls) + " __call__ "
            if not cls.instance:
                cls.instance = Decorated(*args, **kwargs)
            return cls.instance
    return ClassObject()

@singleton
class ASingleton: pass

a = ASingleton()
b = ASingleton()
print(a, b)
print a.__class__.__name__
print ASingleton
assert a is b

@singleton
class BSingleton:
    def __init__(self, x):
        self.x = x

c = BSingleton(11)
d = BSingleton(22)
assert c is d
assert c is not a
In [ ]:
def singleton(klass):
    "Simple replacement of object creation operation"
    def getinstance(*args, **kw):
        if not hasattr(klass, 'instance'):
            klass.instance = klass(*args, **kw)
        return klass.instance
    return getinstance

def singleton(klass):
    """
    More powerful approach: Change the behavior
    of the instances AND the class object.
    """
    class Decorated(klass):
        def __init__(self, *args, **kwargs):
            if hasattr(klass, '__init__'):
                klass.__init__(self, *args, **kwargs)
        def __repr__(self) : return klass.__name__ + " obj"
        __str__ = __repr__
    Decorated.__name__ = klass.__name__
    class ClassObject:
        def __init__(cls):
            cls.instance = None
        def __repr__(cls):
            return klass.__name__
        __str__ = __repr__
        def __call__(cls, *args, **kwargs):
            print str(cls) + " __call__ "
            if not cls.instance:
                cls.instance = Decorated(*args, **kwargs)
            return cls.instance
    return ClassObject()

@singleton
class ASingleton: pass

a = ASingleton()
b = ASingleton()
print(a, b)
print a.__class__.__name__
print ASingleton
assert a is b

@singleton
class BSingleton:
    def __init__(self, x):
        self.x = x

c = BSingleton(11)
d = BSingleton(22)
assert c is d
assert c is not a
In [ ]:
# The custom dictionary
class member_table(dict):
    def __init__(self):
        self.member_names = []

    def __setitem__(self, key, value):
        # if the key is not already defined, add to the
        # list of keys.
        if key not in self:
            self.member_names.append(key)

        # Call superclass
        dict.__setitem__(self, key, value)

# The metaclass
class OrderedClass(type):
    # The prepare function
    @classmethod
    def __prepare__(metacls, name, bases): # No keywords in this case
        return member_table()

    # The metaclass invocation
    def __new__(cls, name, bases, classdict):
        # Note that we replace the classdict with a regular
        # dict before passing it to the superclass, so that we
        # don't continue to record member names after the class
        # has been created.
        result = type.__new__(cls, name, bases, dict(classdict))
        result.member_names = classdict.member_names
        return result
In [ ]:
def meth():
    print("Calling method")

class MyMeta(type):
    @classmethod
    def __prepare__(cls, name, baseClasses):
        return {'meth':meth}

    def __new__(cls, name, baseClasses, classdict):
        return type.__new__(cls, name, baseClasses, classdict)

class Test(metaclass = MyMeta):
    def __init__(self):
        pass

    attr = 'an attribute'

t = Test()
print(t.attr)
In [ ]:
class DictExample:
  def __init__(self):
    self.int_var = 5
    self.list_var = [0,1,2,3,4]
    self.nested_dict = {'a':{'b':2}}
 
# Note that this extends from 'object'; the __slots__ only has an effect
# on these types of 'new' classes
class SlotsExample(object):
  __slots__ = ('int_var','list_var','nested_dict')
 
  def __init__(self):
    self.int_var = 5
    self.list_var = [0,1,2,3,4]
    self.nested_dict = {'a':{'b':2}}
 
# jump to the repl
>>> a = DictExample()
# Here is the dictionary I was talking about.
>>> a.__dict__
{'int_var': 5, 'list_var': [0, 1, 2, 3, 4], 'nested_dict': {'a': {'b': 2}}}
>>> a.x = 5
# We were able to assign a new member variable
>>> a.__dict__
{'x': 5, 'int_var': 5, 'list_var': [0, 1, 2, 3, 4], 'nested_dict': {'a': {'b': 2}}}
 
 
 
>>> b = SlotsExample()
# There is no longer a __dict__ object
>>> b.__dict__
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'SlotsExample' object has no attribute '__dict__'
>>> b.__slots__
('int_var', 'list_var', 'nested_dict')
>>> getattr(b, 'int_var')
5
>>> getattr(a, 'int_var')
5
>>> a.x = 5
# We cannot assign a new member variable; we have declared that there will only
# be member variables whose names appear in the __slots__ iterable
>>> b.x = 5
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'SlotsExample' object has no attribute 'x'
In [ ]:
 
