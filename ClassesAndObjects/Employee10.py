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

Employee.raise_amount=1.05;
'''
Since i am updating the value by using className update will be forawarded
to every object
'''
print(Employee.raise_amount);
print(emp_1.raise_amount);
print(emp_2.raise_amount);

'''
output:
1.05
1.05
1.05
'''

