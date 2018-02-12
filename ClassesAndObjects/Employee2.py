class Employee:
    def __init__(self,fName,lName,pay):
        self.fName=fName;
        self.lName=lName;
        self.pay=pay;
        self.email=fName+"."+lName+"@gmail.com";

emp_1=Employee("Yasir","Choudhary",30000);
emp_2=Employee("Juned","Khan",40000);

print(emp_1.email);
print(emp_2.email);

'''
NOTE:
Employee instance emp_1 & emp_2 is automatically passed to the self
we don't need to pass the self value.

emp_1=Employee("Yasir","Choudhary",30000);
The above statement automatically call Constructor and that also called
as Constructor calling calling statement.

This emp_1=Employee("Yasir","Choudhary",30000); statement call the constructor
like this

    def __init__(emp_1,"Yasir","Choudhary",30000):
        emp_1.fName="Yasir";
        emp_1.lName="Choudhary";
        emp_1.pay=30000;
        emp_1.email="Yasir"+"."+"Choudhary"+"@gmail.com";
'''

'''
OUTPUT:
Yasir.Choudhary@gmail.com
Juned.Khan@gmail.com
'''
