class Employee:
    num_of_Emp=0;
    raise_amt=1.04;

    def __init__(self,fName,lName,pay):
        self.fName=fName;
        self.lName=lName;
        self.pay=pay;
        self.email=fName+"."+lName+"@gmail.com";

        Employee.num_of_Emp+=1;

    def fullName(self):
        return "{} {}".format(self.fName,lName);

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt);

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt=amount;

    @classmethod
    def from_string(cls,emp_str):
        fName, lName, pay = emp_str.split("-");
        return cls(fName, lName, pay);

    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False;
        return True;
        

emp_1 = Employee("Yasir","Choudhary", 6000);
emp_2 = Employee("Juned","Khan",7500);

import datetime
my_date = datetime.date(2018,1,21);
print(Employee.is_workday(my_date));
