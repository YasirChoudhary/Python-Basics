# Single Level Inheritance
class Person:
    value1 = "This is value1";
    value2 = "This is value2";

class Child (Person):
    pass
child=Child();
print(child.value1);
print(child.value2);
