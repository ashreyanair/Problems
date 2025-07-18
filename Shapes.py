#with argument with return type
def circle(r):
    ca=3.14*r*r
    return ca

def square(s):
    sa=s*s
    return sa

def triangle(a,b):
    ta=0.5*a*b
    return ta

def rectangle(l,b):
    ra=l*b
    return ra

while(True):
    print("1. Circle")
    print("2. Square")
    print("3. Triangle")
    print("4. Rectangle")

    print("0. EXIT")

    ch=int(input("enter ur choice"))
    if ch==0:
        exit()

    elif ch==1:
        i=int(input("enter the radius of  circle "))
        c=circle(i)
        print(c)
    elif ch==2:
        s=int(input("enter the side of the square"))
        sq=square(s)
        print(sq)
    elif ch==3:
        a=int(input("enter the side a"))
        b=int(input("enter the side b "))
        tr=triangle(a,b)
        print(tr)
    elif ch==4:
        l=int(input("enter length "))
        b=int(input("enter breadth "))
        rec=rectangle(l,b)
        print(rec)
    else:
        print("INVALID")



