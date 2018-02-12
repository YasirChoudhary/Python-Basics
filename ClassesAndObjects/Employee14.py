class Employee:
    num_of_Emp=0;
    raise_amt=1.04;

    def __init__(self,fName,lName,pay):
        self.fName=fName;
        self.lName=lName;
        self.pay=pay;
        self.email=lName+"."+lName+"@gmail.com";

        Employee.num_of_Emp+=1;

    def fullName(self):
        return "{} {}".format(self.fName,lName);

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt);

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt=amount;

emp_1 = Employee("Yasir","Choudhary", 6000);
emp_2 = Employee("Juned","Khan",7500);

emp_1.set_raise_amt(1.05);
#The above statement will also change values everywhere
print(Employee.raise_amt);
print(emp_1.raise_amt);
print(emp_2.raise_amt);
