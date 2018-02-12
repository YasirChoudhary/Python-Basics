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

emp_1.raise_amount=1.05;#since i am updating the instance the variable update will be done only for tha particula instance.
'''
The above statment will also create the instance variable raise_amount
for emp_1 only
'''
print(emp_1.__dict__);
print(Employee.raise_amount);
print(emp_1.raise_amount);
print(emp_2.raise_amount);

'''
Output:
{'raise_amount': 1.05, 'lName': 'Choudhary',
'email': 'Yasir.Choudhary@gmail.com',
'fName': 'Yasir', 'pay': 30000}
1.04
1.05
1.04
'''
