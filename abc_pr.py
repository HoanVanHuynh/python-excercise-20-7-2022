from abc import ABC, abstractmethod 
# abc is a builtin module, we have to import ABC and abstractmethod

class Animal(ABC): # Inherit from ABC(Abstract base class)
    
    @abstractmethod # Decorator to define an abstract method 
    def feed(self):
        pass

class Panda(Animal):
    def wrong_name(self):
        print("Feeding a panda with some tasty bamboo!")    

    def feed(self):
        print("Feeding a panda")

class Snake(Animal):
    def wrong_name(self):
        print("please use another method")
    
    def feed(self):
        print("Feedin a snake")
    
    def feed_2(self):
        return self

    def feed_e(self, fun):
        return fun
class Lion(Animal):
    pass

