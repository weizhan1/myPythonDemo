from bdb import bar
def foo(bar):
    return bar+1

print type(foo)

def call_foo_with_arg(foo, arg):
    return foo(arg)

print call_foo_with_arg(foo, 5)

def parent():
    print "Print from the parent function"
    
    def first_child():
        return "Print from first_child function"
    
    def second_child():
        return "Print from second child function"
    
    print first_child()
    print second_child()

print parent()

def parent(num):
        
    def first_child():
        return "Print from first_child function"
    
    def second_child():
        return "Print from second child function"

    try:
        assert num == 10
        return first_child
    except AssertionError:
        return second_child
    
foo = parent (10)
bar = parent (11)

print foo
print bar

print foo()
print bar()

def my_decorator(some_function):
    
    def wrapper():
        print "something is happening before some_function is called"
        
        num = 10
        
        if num == 10:
            print "Yes"
        else:
            print "No"
            
        some_function()
        
        print "something is happening after some_function is called"
        
    return wrapper

def just_some_function():
    print "Wheeee ...."
    
just_some_function = my_decorator(just_some_function)

just_some_function()

if __name__ == "__main__":
    my_decorator()

from decor1 import import my_decorator

