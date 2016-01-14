## Animal is-a object, Look at the extra credit
class Animal(object):
    pass

## Dog is a class that is-a Animal and has-a __init__ that takes self and name parameters
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## Cat is a class that is-a Animal and has-a __init__ that takes self and name parameters
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## Person is an object and has-a __init__ that takes self and name parameters
class Person(object):

    def __init__(self, name):
        ## __init__ takes self and name parameters
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person and has-a init that takes self, name and salary as parameters
class Employee(Person):

    def __init__(self, name, salary):
        ##
        super(Employee, self).__init__(name)
        self.salary = salary