#Employee details
class Emp:
    #class variable or static-common across all the objects
    emp_comp='IBM'
    count = 0
    #constructors-used initialize value inside of an object------------->(madatory)
    def __init__(self,emp_id,emp_name):
        #object level variable or Non-static (changes from object to object)
        self.emp_id=emp_id
        self.emp_name=emp_name
        print("Emp Id:",self.emp_id)
        print("Emp Name:",self.emp_name)
        #accessing the class variable
        print("Emp Comp:",Emp.emp_comp)
        Emp.count=Emp.count+1
    #class level methods -common across all the objects
    #It should have decorators at the class
    #It should have 1st argument as cls
    @classmethod   #decorators
    def cm1(cls,emp_position):
        cls.emp_position=emp_position
        print("Emp position:",cls.emp_position)
    @classmethod
    def cm2(cls,emp_roll):
        cls.emp_roll=emp_roll
        print("Emp Roll:",cls.emp_roll)
    @classmethod
    def cm3(cls):
        cls.work_place='Bangalore'
        print("Emp Work Place:",cls.work_place)

    #instance method or object level methods----------->(optional)
    #It is used to perform object level operation
    #It should have 1st arg as a self
    def im1(self,emp_sal):
        self.emp_sal=emp_sal
        print("Emp Sal:",self.emp_sal)
    def im2(self,emp_insurance):
        self.emp_insurance=emp_insurance
        print("Emp Insurance:",emp_insurance)
#creating the object e1
e1=Emp(21435687,'Hari')
#accessing class methods using class name
Emp.cm1('Senior level-I')
Emp.cm2('On roll')
Emp.cm3()
#Accessing Instance methods using reference variable
e1.im1(40000.00)
e1.im2(1500000.00)
print("No of objects created:",Emp.count)
print()
#creating the object e2
e2=Emp(21435697,'Rahul')
#accessing class methods using class name
Emp.cm1('Senior level-II')
Emp.cm2('On roll')
Emp.cm3()
#Accessing Instance methods using reference variable
e2.im1(50000.00)
e2.im2(2000000.00)
print("No of objects created:",Emp.count)
print()
print("Single inheritance:")
#Base class----->Derived class(Base class)
#A------->B(A)
#It is used for code reusablity
#There are Parent and child
class Flight():
    #class varaiable
    fname='IX181'
    count=0
    #constructor -initialize values inside of an object
    def __init__(self,fnum):
        self.fnum=fnum
        print("Flight Num:",self.fnum)
        print("Flight Name:",Flight.fname)
        Flight.count=Flight.count+1
    #Instance methods or object level method
    def flying(self,flyheight):
        self.flyheight=flyheight
        print("Flight Height is {} Feet".format(self.flyheight))
    def running(self,flyrun):
        self.flyrun=flyrun
        print("Flight Running At {} km Speed ".format(self.flyrun))
    def seat(self,seattype):
        self.seattype=seattype
        print("Passenger seatType:",self.seattype)
f1=Flight(234567)
f1.flying(7000)
f1.running(120)
f1.seat('semi sleeper')
print("No of object is created:",Flight.count)
print()
#inherits from base class
class Flight1(Flight):
    #Here if you want to initialize any objects you can def constructors ,otherwise PVM will create it
    #Instance methods or object level method
    def ac(self,ac_cond):
        self.ac_cond=ac_cond
        print("Ac Working At {} Temp".format(self.ac_cond))
    def seat(self,seattype):
        self.seattype=seattype
        print("Passenger seatType:",self.seattype)
f2=Flight1(234569)
f2.flying(5000)
f2.running(100)
f2.ac('Normal')
f2.seat('Sleeper')
print("No of object is created:",Flight.count)
print()
print("Multilvel inheritance")
#Base class()---------->Base class2(Base class) --------->Base class3(Parent class2)------>derived class(child class)
class Flight1():
    #class varaiable
    fname='IX181'
    count=0
    #constructor -initialize values inside of an object
    def __init__(self,fnum):
        self.fnum=fnum
        print("Flight Num:",self.fnum)
        print("Flight Name:",Flight.fname)
        Flight1.count=Flight1.count+1
    #Instance methods or object level method
    def flying(self,flyheight):
        self.flyheight=flyheight
        print("Flight Height is {} Feet".format(self.flyheight))
    def running(self,flyrun):
        self.flyrun=flyrun
        print("Flight Running At {} km Speed ".format(self.flyrun))
    def seat(self,seattype):
        self.seattype=seattype
        print("Passenger seatType:",self.seattype)
f1=Flight1(234567)
f1.flying(7000)
f1.running(120)
f1.seat('semi sleeper')
print("No of object is created:",Flight1.count)
print()
#inherits from base class
class Flight2(Flight1):
    #Here if you want to initialize any objects you can def constructors ,otherwise PVM will create it
    #Instance methods or object level method
    def ac(self,ac_cond):
        self.ac_cond=ac_cond
        print("Ac Working At {} Temp".format(self.ac_cond))
    def seat(self,seattype):
        self.seattype=seattype
        print("Passenger seatType:",self.seattype)
f2=Flight2(234569)
f2.flying(5000)
f2.running(100)
f2.ac('Normal')
f2.seat('Sleeper')
print("No of object is created:",Flight1.count)
print()
class Flight3(Flight2):
    #instance methods or object level method
    def fuelcapacity(self,fuelcap):
        self.fuelcap=fuelcap
        print("Fuel Capacity {} ltr".format(self.fuelcap))
    def transition(self,airtransistion):
        self.airtransition=airtransistion
        print("Air Transistion type:",self.airtransition)
f3=Flight3(234572)
f3.flying(5500)
f3.running(110)
f3.ac('Medium cool')
f3.seat('semi sleeper')
f3.fuelcapacity(2400)
f3.transition('1 Transition')
print("No of object is created:",Flight1.count)
print()
print("Mutiple inheritance:")
#Multiple inheritance:Base class1------>Base class2(Base class1)-------->Base class3(Base class2,Base class1)
#Multiple inheritance:A--->B(A)---------->C(B,A)