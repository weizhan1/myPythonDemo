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

if __name__ == "__main__":
    my_decorator()