"""1.Abstract Class
Outline:
Write a program to create a base class that consists of two functions 
- one to display a value, and another function is an abstract method
. Next, create a subclass that consists of a method similar to the abstract method.
 Finally, showcase how Abstraction is being implemented in this example."""
"""from abc import ABC,abstractmethod
class Parent(ABC):
    def print(self,x):
        print("The given value is ",x)
    @abstractmethod
    def task(self):
        print("We are inside parent class task")
class Child(Parent):
    def task(self):
        print("We are inside child class task")
new_object = Child()
new_object.task()
new_object.print(100)"""

"""2.Class Animal
Outline:
Write a program to implement abstraction on animal class (base class).
The abstract method will be move will display what subclasses can do.
Subclasses can be something like - Human, Dog."""
"""from abc import ABC,abstractmethod
class Animal(ABC):
    def move(self):
        pass
#Sub classes
class Human(Animal):
    def move(self):
        print("Human-I can walk and run")
h = Human()
h.move()
class Dog(Animal):
    def move(self):
        print("Dog-I can fetch a ball")
d = Dog()
d.move()
class Lion(Animal):
    def move(self):
        print("Lion-I can roar loudly")
l = Lion()
l.move()"""

"""3All about Countries
Outline:
Write a program to create two classes for two different countries that consist of three methods to display the following
 information of respective country - 
 capital, language and type of country
 . Then, use Polymorphism to create a common interface for both classes."""
class India():
    def capital(self):
        print("New Delhi is the capital of India.")
    def language(self):
        print("Hindi is the most widely spoken language of India.")
    def type(self):
        print("India is a developing country.")
class USA():
    def capital(self):
        print("Washington is the capital of USA.")
    def language(self):
        print("English is the most widely spoken language of USA.")
    def type(self):
        print("USA is a developed country.")
object1 = India()
object2 = USA()
for i in (object1,object2):
    i.capital()
    i.language()
    i.type()