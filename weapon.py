from abc import ABCMeta, abstractmethod 

class Weapon(metaclass=ABCMeta):

    def __init__(self):
        print("Weapon object created...")

    @abstractmethod
    def aim(self):
        pass 

    @abtractmethod
    def fire(self):
        pass 

    