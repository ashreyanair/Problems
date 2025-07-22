class rectangle:

    p1="1.sum of all angle is 360"
    p2="2. each and every angle is 90"
    def calc(self):
        a=int(input("enter the length of rectsngle"))
        b=int(input("enter the breadth of rectangle "))
        self.len=a
        self.breadth=b

    def calculation(self):
        print("area is ",self.len*self.breadth)
        print("perimeter is ",2*self.len*self.breadth)

s1=rectangle()
s2=rectangle()
print(rectangle.p1)
print(rectangle.p2)
s1.calc()
s1.calculation()
s2.calc()

s2.calculation()