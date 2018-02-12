# Multiple Inheritance
class Person1:
    value1 = "This is value1";
    value2 = "This is value2";

class Person2:
    value3 = "This is value3";
    value4 = "This is value4";
    
class Child (Person1, Person2):
    pass
child=Child();
print(child.value1);
print(child.value2);
print(child.value3);
print(child.value4);
