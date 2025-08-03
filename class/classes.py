from abc import ABC, abstractmethod

class Base(ABC):
    def __init__(self, name, pin):
        self.name = name
        self.__private = pin
        self.pin = pin
    
    @abstractmethod
    def check(self):
        retself.pin = "ABC Pin"

class Std(Base):
    def check(self):
        return self.pin
        

obj = Std("qud", "pin")
print(obj.name)
print(obj.check())
