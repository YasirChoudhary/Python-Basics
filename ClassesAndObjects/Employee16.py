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
        

emp_1 = Employee("Yasir","Choudhary", 6000);
emp_2 = Employee("Juned","Khan",7500);

emp_str_3 = "Sarafaraz-Ansari-7100";
emp_str_4 = "Saeed-Shaikh-8000";

emp_3 = Employee.from_string(emp_str_3);

print(emp_3.email);
print(emp_3.pay);
