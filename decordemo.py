>> from functools import wraps
>>> def my_decorator(f):
...     @wraps(f)
...     def wrapper(*args, **kwds):
...         print('Calling decorated function')
...         return f(*args, **kwds)
...     return wrapper
...
>>> @my_decorator
... def example():
...     """Docstring"""
...     print('Called example function')
...

from decorator import my_decorator
from _ast import Num

@my_decorator
def just_some_function():
    print "Wheeee..."
    
just_some_function()

import time

def timing_function(some_function):
    """
    output the time a function takes to execute.
    """
    
    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2-t1)) + "\n"
    return wrapper

@timing_function
def my_function():
    num_list = []
    for x in range(0,10000):
        num_list.append(x)
    print "\nSum of all the numbers: "+str((sum(num_list)))
    
print my_function()

from time import sleep

def sleep_decorator(function):
    """
    limits how fast the function is called.
    """
    
    def wrapper(*args, **kwargs):
        sleep(2)
        return function(*args, **kwargs)
    return wrapper

@sleep_decorator
def print_number(num):
    return num 

print print_number(222)

for x in range(1, 6):
    print print_number(x)
    
    
from functools import wraps
from flask import g, request, redirect, url_for
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

if __name__ == '__main__':
    app.run()


# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if g.user is None:
#             return redirect(url_for('login', next=request.url))
#         return f(*args, **kwargs)
#     return decorated_function
# 
# @app.route('/secret')
# @login_required
# def secret():
#     pass

