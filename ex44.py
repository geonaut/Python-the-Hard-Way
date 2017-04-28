class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

#both return "PARENT implicit()", as child has no implict function
dad.implicit()
son.implicit()

#returns "PARENT override()"
dad.override()
#returns child.override(), because child.override() overrides parent.override()
son.override()

#returns parent altered(), as expected
dad.altered()
#returns 3 lines - print > parent altered() > print, because super is used to access the parent function once
son.altered()

class Other(object):

    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"

class ChildTwo(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "CHILDTWO override()"

    def altered(self):
        print "CHILDTWO, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILDTWO, AFTER OTHER altered()"

son = ChildTwo()

son.implicit()
son.override()
son.altered()