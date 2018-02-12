class Person:
    def setName(self,firstName,lastName):
        self.firstName=firstName;
        self.lastName=lastName;

    def printName(self):
        print(self.firstName,"",self.lastName);

firstPerson=Person();
firstPerson.setName("Yasir","Choudhary")
firstPerson.printName()

secPerson=Person();
secPerson.setName("Sarfaraz","Ansari")
secPerson.printName()
