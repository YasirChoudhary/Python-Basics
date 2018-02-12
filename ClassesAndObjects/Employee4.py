class Employee:
    def __init__(self,fName,lName,pay):
        self.fName=fName;
        self.lName=lName;
        self.pay=pay;
        self.email=fName+"."+lName+"@gmail.com";

    def fullName(self):
        return "{} {}".format(self.fName,self.lName);

emp_1=Employee("Yasir","Choudhary",30000);
emp_2=Employee("Juned","Khan",40000);

print(emp_1.email);

print(emp_1.fullName());

#The other way of printing FullName is by calling ClassName.memberName(instace);
print(Employee.fullName(emp_2));

#print("{} {}".format(emp_1.fName,emp_1.lName));

'''
NOTE:
Each Method in a class automatically takes an instance as the first
argument which can be done by defining self variable.
'''

'''
OUTPUT:
Yasir.Choudhary@gmail.com
Yasir Choudhary
Juned Khan
'''
