#Subclassing object in Python 2 notation
class Animal(object):
    pass

#Dog is-a subclass of animal (sub class of object)
class Dog(Animal):

    def __init__(self, name):
        #instatinating object requires a name, which becomes self.name
        self.name = name

#Cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        #instatinating object requires a name, which becomes self.name
        self.name = name

#person is an object
class Person(object):

    def __init__(self, name):
        #instatinating object requires a name, which becomes self.name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

#Employee is a subclass of person
class Employee(Person):

    def __init__(self, name, salary):
         #instatinating object requires a name, which becomes self.name, as well as salary
         #super calls init in the parent object, so the name is attached as self.name
        super(Employee, self).__init__(name)
        #salart doesn't exist in the parent object, so is set here
        self.salary = salary

#Fish is a new object
class Fish(object):
    pass

#Salmon is a type of fish
class Salmon(Fish):
    pass

#Another type of fish
class Halibut(Fish):
    pass


#instantiating a dog with name Rover
rover = Dog("Rover")

#instantiating a cat named Satan
satan = Cat("Satan")

#istantiating a person named mary
mary = Person("Mary")

#defining mary's pet
mary.pet = satan

#instantiating a new employee, passing name and salary
frank = Employee("Frank", 120000)

#defining Frank's pet, via the person class
frank.pet = rover

#Flipper is a new fish
flipper = Fish()

#Crouse is a new salmon
crouse = Salmon()

#Harry is a Halibut, but this is a name, so might be better passed as Halibut('Harry')
harry = Halibut()