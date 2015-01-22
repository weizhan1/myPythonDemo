class Parent:
    parentAttr = 100
    def __init__(self):
        print "Calling parent constructor"
    
    def parentMethod(self):
        print 'Calling parent method'
        
    def setAttr(self, attr):
        Parent.parentAttr = attr
        
    def getAttr(self):
        print "Parent attribute :", Parent.parentAttr
        
    def myMethod(self):
        print "Calling parent myMethod"
        
class Grandparent:
    grandparentAttr = 300
    def __init__(self):
        print "Calling grandparent constrcutor"
        
    def grandparentMethod(self):
        print "Calling grandparent method"
        
class Child(Parent, Grandparent):
    
    def __init__(self):
        print "Calling child constructor"
    
    def childMethod(self):
        print 'Calling child method'
        
    def myMethod(self):
        print "Calling child myMethod"
        
c = Child()
c.myMethod()
c.childMethod()
c.parentMethod()
c.grandparentMethod()
c.setAttr(200)
c.getAttr()
     