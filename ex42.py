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
        ## TODO Answer
        super(Employee, self).__init__(name)
        self.salary = salary


## Fish is an object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## Mary has-a pet
mary.pet = satan

## frank is-a Employee with a Salary
frank = Employee("Frank", 120000)

## frank has-a pet
frank.pet = rover

## flipper is-a instance of Fish
flipper = Fish()

## crouse is-a instance of Salmon
crouse = Salmon()

## harry is-a instance of Halibut
harry = Halibut()
