class emp:
    profit=1000000
    tax=10
    company="COGNIZANT"
    def __init__(self,name,sal,age,per):
        self.name=name
        self.sal=sal
        self.age=age
        self.per=per
        self.tax_amount=0
        self.share_amount=0

    def cal_tax(self):
        return((emp.tax/100)*self.sal)
    def cal_share(self):
        return((self.per/100)*emp.profit)
    def display(self):
        print("1.",self.name)
        print("2.", emp.company)
        print("3.", self.age)
        print("4.", self.sal)
        print("5.",self.cal_tax())
        print("6.",self.cal_share())
a1=emp("SACHIN",50000,40,5)
a2=emp("SHREYA",40000,35,2)

a1.display()
print("--------------")
a2.display()
