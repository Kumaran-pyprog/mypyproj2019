#Take an Example of Mobile phone
from abc import ABC,abstractmethod
#print("Abstraction class:")
#Abstraction class
class Mobile1(ABC):
    #implemention done for dialpad but talk we have only idea.
    def dialpad(self):
        print("DialPad Features implemented")
    @abstractmethod
    def talk(self):
        pass
#create object
#print("Year:1900")
#b=Mobile1()
#b.dialpad()
#print("Don't have idea to implement Talk feature")
#b.talk()
#print()
print("Concreteclass:")
#Concreteclass-Dialpad and talk features are implemented
class Mobile2(Mobile1):
    #class variable
    tel_name='BinaTone'
    #constructors
    def __init__(self,tel_model):
        self.tel_model=tel_model
        print("Telephone Model:",self.tel_model)
    #Instance method or object level method
    def talk(self):
        print("Talk Features implemented")
#create the object
print("Year:1940")
c=Mobile2('Landline')
print("Telephone Name:",Mobile2.tel_name)
#call Instance method or object method through reference variable
c.dialpad()
c.talk()
print()
print("Concreteclass:")
class Mobile3(Mobile2):
    #class variable or static
    mob_name='NOKIA'
    #constructors
    def __init__(self,mob_model,mob_imei):
        self.mob_model=mob_model
        self.mob_imei=mob_imei
        print("Mobile Model:",self.mob_model)
        print("Mobile IMEI:",self.mob_imei)
    #Instance method
    def rearcam(self):
        self.mob_rearcam=4
        print("Mobile Rear camera {} MP".format(self.mob_rearcam))
print("Year:1992")
print("Mobile Name:",Mobile3.mob_name)
d=Mobile3(2200,'346798ABC123')
d.dialpad()
d.talk()
d.rearcam()
print()
print("Concreteclass:")
class Mobile4(Mobile3):
    #constructors
    def __init__(self,mob_osver,mob_model,mob_imei):
        self.mob_osver=mob_osver
        print("Mobile Osversion:", self.mob_osver)
        Mobile3.__init__(self,mob_model,mob_imei)
    #Instance method
    def touchpad(self):
        print("Touchpad features implemented")
    def frontcam(self):
        self.mob_frontcam=2
        print("Mobile Front camera {} MP".format(self.mob_frontcam))
    def storage(self):
        self.int_storage=16
        print("Mobile Internal Storage {} GB".format(self.int_storage))
#create the object
print("year:2010")
print("Mobile Name:",Mobile3.mob_name)
e=Mobile4('Android',3.2,'23456KFC986')
e.talk()
e.touchpad()
e.rearcam()
e.frontcam()
e.storage()
print()
print("Method overriding:")
print("Concreteclass:")
#Methodoverriding or polymorphism-Enhancing the existing feature
#For method overriding inheritance is mandatory
class Mobile5(Mobile4):
    #class variable
    mob_name2='APPLE'
    #constructor
    def __init__(self,mob_osver,mob_model,mob_imei):
        Mobile4.__init__(self,mob_osver,mob_model,mob_imei)
    #instance method
    def rearcam(self):
        self.mob_rearcam=12
        print("Mobile Rear camera {} MP".format(self.mob_rearcam))
    def frontcam(self):
        self.mob_frontcam=4
        print("Mobile Front camera {} MP".format(self.mob_frontcam))
    def storage(self):
        self.int_storage=64
        print("Mobile Internal Storage {} GB".format(self.int_storage))
#create the object
print("Year:2015")
print("Mobile Name:",Mobile5.mob_name2)
f=Mobile5('IOS','iPhone6','34567KGF983')
f.talk()
f.touchpad()
f.rearcam()
f.frontcam()
f.storage()



