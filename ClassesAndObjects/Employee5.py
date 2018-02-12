class Employee:
    def __init__(self,fName,lName,pay):
        self.fName=fName;
        self.lName=lName;
        self.pay=pay;
        self.email=fName+'.'+lName+'@gmail.com';

    def fullName(self):
        return '{} {}'.format(self.fName,self.lName);

    def apply_raise(self):
        self.pay=int(self.pay*1.04);

emp_1=Employee("Yasir","Choudhary",30000);
emp_2=Employee("Juned","Khan",65000);

print(emp_1.pay);
emp_1.apply_raise();
print(emp_1.pay);
