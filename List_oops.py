class rect:
    def set_dim(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        return(self.a*self.b)
nums=[]
d=int(input("Enter the number of rectangles: "))
for i in range(d):
    R=rect()
    a=int(input("Enter the length of rectangle: "))
    b = int(input("Enter the breadth of rectangle: "))
    R.set_dim(a,b)
    nums.append(R)
iii=1
for i in nums:
    print("Area of rectangle {} is : {}".format(iii,i.area()))
    iii=iii+1

