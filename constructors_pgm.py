class Employee:
    speed=300
    def __init__(self,id,name,a,b,ac_name,ac_vol,ac_warranty):
        self.id =id
        self.name=name
        self.a=a
        self.b=b
        self.ac_name=ac_name
        self.ac_vol=ac_vol
        self.ac_warranty=ac_warranty
    def addval(self):
        return self.a + self.b
    def fun(self):
        print("Hi",self.name,"your id is ",self.id)
    def run(self):
        print("your running speed is ",self.speed)
    def acfeatures(self):
        print("AC Name: ",self.ac_name,"ac_vol: ",self.ac_vol,"ac_warraanty: ",self.ac_warranty)
obj=Employee(123,'ashok',12,13,'voltas',230,5)
print(obj.id)
print(obj.name)
print(obj.addval())
obj.fun()
obj.run()
obj.acfeatures()

