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

print(Employee.__dict__);


'''
Output:
{'__module__': '__main__', 'apply_raise': <function Employee.apply_raise at 0x7fc3b367a400>,
'__init__': <function Employee.__init__ at 0x7fc3ba3362f0>,
'fullName': <function Employee.fullName at 0x7fc3b367a378>,
'raise_amount': 1.04,
'__dict__': <attribute '__dict__' of 'Employee' objects>,
'__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}
'''

#Employee is having the raise_amount in it's name space because it is a class variable.
