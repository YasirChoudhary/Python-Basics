class Employee:
    raise_amount=1.04;
    numberOfEmp=0;
    def __init__(self,fName,lName,pay):
        self.fName=fName;
        self.lName=lName;
        self.pay=pay;
        self.email=fName+'.'+lName+'@gmail.com';

        Employee.numberOfEmp +=1;

    def fullName(self):
        return '{} {}'.format(self.fName,self.lName);

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount);

print(Employee.numberOfEmp);
emp_1=Employee("Yasir","Choudhary",30000);
emp_2=Employee("Juned","Khan",65000);
print(Employee.numberOfEmp);

'''
Output:
0
2
'''

'''
NOTE:
If you want to make a variable static throughout the program
than update the variable by using className.Membername like
Employee.numberOfEmp +=1; and also access the variable by using
className.Membername
'''
