class Employee:
    raise_amount=1.04;
    def __init__(self,fName,lName,pay):
        self.fName=fName;
        self.lName=lName;
        self.pay=pay;
        self.email=fName+'.'+lName+'@gmail.com';

    def fullName(self):
        return '{} {}'.format(self.fName,self.lName);

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount);

emp_1=Employee("Yasir","Choudhary",30000);
emp_2=Employee("Juned","Khan",65000);

print(Employee.raise_amount);
print(emp_1.raise_amount);
print(emp_2.raise_amount);


'''
Output:
1.04
1.04
1.04
'''
