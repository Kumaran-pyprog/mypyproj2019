from abc import ABC,abstractmethod
class Flight1(ABC):
    #instance method
    def run(self):
        print("Running......!!!!")
    @abstractmethod
    def fly(self):
        pass
class Flight2(Flight1):
    def fly(self):
        print("Flying........!!!!")
a=Flight2()
a.run()
a.fly()