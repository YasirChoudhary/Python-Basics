class Employee:
    def __init__(self):
        print("Our class object is created");
    def __del__(self):
        print("Our class object is destroyed"); 
    def setName(self,firstName,lastName):
        self.firstName=firstName;
        self.lastName=lastName;
    def printName(self):
        print(self.firstName,self.lastName);

employee=Employee();
employee.setName("Yasir","Choudhary");
employee.printName();
employee.__del__();
employee.printName();
