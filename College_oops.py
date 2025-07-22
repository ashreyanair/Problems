class college:
    col="NITTE"
    def student(self,name,mark):
        self.name=name
        self.mark=mark
    def passfail(self):
        if self.mark>40:
            print("passs")
        else:
            print("fail")
    def modify(self,grace):
        self.mark=self.mark+grace
    def display(self):
        print("name ",self.name)
        print("college ",self.col)
        print("marks ",self.mark)
        self.passfail()
s1=college()
s2=college()
s1.student("nick",56)
s2.student("pooja",34)
s1.passfail()
s2.passfail()
s2.modify(70)
s2.passfail()
s1.display()
s2.display()
print(college.col)