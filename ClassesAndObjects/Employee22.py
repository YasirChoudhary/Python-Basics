class Employee:
    raise_amt=1.04;

    def __init__(self,first,last,pay):
        self.first=first;
        self.last=last;
        self.pay=pay;
        self.email=first+"."+last+"@gmail.com";

    def fullname(self):
        return '{} {}'.format(self.first,self.last);

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt);


class Developer(Employee):
    raise_amt=1.10;

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay);
        self.prog_lang=prog_lang;
    

dev_1 = Developer("Yasir","Choudhary",50000,"Python");
dev_2 = Developer("Sarfaraz","Ansari",60000,"java");


print(dev_1.email);
print(dev_1.prog_lang);

