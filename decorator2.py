In [4]:

class my_decorator(object):
​
    def __init__(self, f):
        print("inside my_decorator.__init__()")
        f() # Prove that function definition has completed
​
    def __call__(self):
        print("inside my_decorator.__call__()")
        
@my_decorator
def aFunction():
    print("inside aFunction()")
    
print("Finished decorating aFunction()")
​
aFunction()
    
    
inside my_decorator.__init__()
inside aFunction()
Finished decorating aFunction()
inside my_decorator.__call__()
In [6]:

class entry_exit(object):
​
    def __init__(self, f):
        self.f = f
​
    def __call__(self):
        print("Entering", self.f.__name__)
        self.f()
        print("Exited", self.f.__name__)
​
@entry_exit
def func1():
    print("inside func1()")
    
@entry_exit
def func2():
    print("inside func2()")
​
func1()
func2()
Entering func1
inside func1()
Exited func1
Entering func2
inside func2()
Exited func2
In [7]:

def entry_exit(f):
    def new_f():
        print("Entering", f.__name__)
        f()
        print("Exited", f.__name__)
    return new_f
​
@entry_exit
def func1():
    print("inside func1()")
​
@entry_exit
def func2():
    print("inside func2()")
​
func1()
func2()
print(func1.__name__)
Entering func1
inside func1()
Exited func1
Entering func2
inside func2()
Exited func2
new_f
In [8]:

def entry_exit(f):
    def new_f():
        print("Entering", f.__name__)
        f()
        print("Exited", f.__name__)
    new_f.__name__ = f.__name__
    return new_f
In [9]:

class decorator_without_arguments(object):
​
    def __init__(self, f):
        """
        If there are no decorator arguments, the function
        to be decorated is passed to the constructor.
        """
        print("Inside __init__()")
        self.f = f
​
    def __call__(self, *args):
        """
        The __call__ method is not called until the
        decorated function is called.
        """
        print("Inside __call__()")
        self.f(*args)
        print("After self.f(*args)")
​
@decorator_without_arguments
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)
​
print("After decoration")
​
print("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print("After first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print("After second sayHello() call")
Inside __init__()
After decoration
Preparing to call sayHello()
Inside __call__()
sayHello arguments: say hello argument list
After self.f(*args)
After first sayHello() call
Inside __call__()
sayHello arguments: a different set of arguments
After self.f(*args)
After second sayHello() call
In [10]:

class decorator_with_arguments(object):
​
    def __init__(self, arg1, arg2, arg3):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        print("Inside __init__()")
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
​
    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        print("Inside __call__()")
        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", self.arg1, self.arg2, self.arg3)
            f(*args)
            print("After f(*args)")
        return wrapped_f
​
@decorator_with_arguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)
​
print("After decoration")
​
print("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print("after first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print("after second sayHello() call")
Inside __init__()
Inside __call__()
After decoration
Preparing to call sayHello()
Inside wrapped_f()
Decorator arguments: hello world 42
sayHello arguments: say hello argument list
After f(*args)
after first sayHello() call
Inside wrapped_f()
Decorator arguments: hello world 42
sayHello arguments: a different set of arguments
After f(*args)
after second sayHello() call
In [11]:

def decorator_function_with_arguments(arg1, arg2, arg3):
    def wrap(f):
        print("Inside wrap()")
        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", arg1, arg2, arg3)
            f(*args)
            print("After f(*args)")
        return wrapped_f
    return wrap
​
@decorator_function_with_arguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)
​
print("After decoration")
​
print("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print("after first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print("after second sayHello() call")
Inside wrap()
After decoration
Preparing to call sayHello()
Inside wrapped_f()
Decorator arguments: hello world 42
sayHello arguments: say hello argument list
After f(*args)
after first sayHello() call
Inside wrapped_f()
Decorator arguments: hello world 42
sayHello arguments: a different set of arguments
After f(*args)
after second sayHello() call
In [40]:

from weakref import WeakValueDictionary
​
class Counter:
    _instances = WeakValueDictionary()
    @property
    def Count(self):
        return len(self._instances)
​
    def __init__(self, name):
        self.name = name
        self._instances[id(self)] = self
        print(name, 'created')
​
    def __del__(self):
        print(self.name, 'deleted')
        if self.Count == 0:
            print('Last Counter object deleted')
        else:
            print(self.Count, 'Counter objects remaining')
​
x = Counter("First")
​
First created
First deleted
1 Counter objects remaining
