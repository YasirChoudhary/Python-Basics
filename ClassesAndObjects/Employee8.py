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

print(emp_1.__dict__);


'''
Output:
{'pay': 30000, 'fName': 'Yasir', 'lName': 'Choudhary',
'email': 'Yasir.Choudhary@gmail.com'}
'''

#emp_1 is not having the attribute raise_amount in it's name-space
