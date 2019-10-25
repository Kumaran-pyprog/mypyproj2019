class Emp:
    #class variable or static
    emp_comp='CISCO'
    count=0
    #constructors
    def __init__(self):
        print(Emp.emp_comp)
        Emp.count=Emp.count+1
e1=Emp()
#print("No of objects created:",e1.count)
print("No of objects created:",Emp.count)
e2=Emp()
#print("No of objects created:",e2.count)
print("No of objects created:",Emp.count)
e3=Emp()
#print("No of objects created:",e3.count)
print("No of objects created:",Emp.count)
e4=Emp()
#print("No of objects created:",e4.count)
print("No of objects created:",Emp.count)
