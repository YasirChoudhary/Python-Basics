class Employee:
    def __init__(self,fName,lName,pay):
        self.fName=fName;
        self.lName=lName;
        self.pay=pay;
        self.email=fName+"."+lName+"@gmail.com";

emp_1=Employee("Yasir","Choudhary",30000);
emp_2=Employee("Juned","Khan",40000);

print("{} {}".format(emp_1.fName,emp_1.lName));

'''
Yasir Choudhary
'''
