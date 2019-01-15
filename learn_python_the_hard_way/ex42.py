## Animal is a object
class Animal(object):
  pass

## Dog is-a Animal
class Dog(Animal):
  def __init__(self, name):
    self.name = name


## Cat is-a Animal
class Cat(Animal):
  def __init__(self, name):
    self.name = name

## Person is a object
class Person(object):
  def __init__(self, name):
    self.name = name
    self.pet = None

## Employee is a person
class Employee(Person):
  def __init__(self, name, salary):
    super(Employee, self).__init__(name)
    self.salary = salary

  def __str__(self):
    return "{} attributes:\n Salary: {} salary\nName: {}\nPet: {}\n".format(type(self), self.salary, self.name, self.pet)


# Fish is a object
class Fish(object):
  pass

# Salmon is a rtype of Fish
class Salmon(Fish):
  pass

# Halibut is a type of Fish
class Halibut(Fish):
  pass

## rover is a dog
rover = Dog("rover")

## satan is a cat
satan = Cat("satan")

## mary is a person
mary = Person("Mary")

## mary has-a pet which is a cat
mary.pet = satan

## frank is an employee
frank = Employee("Frank", salary=120000)

## frank has-a dog
frank.pet = rover

print(frank)

## flipper is a fish
flipper = Fish()

## crouse is a salmon
crouse = Salmon()

## harry is a halibut
harry = Halibut()
print(type(harry))
print(harry)
