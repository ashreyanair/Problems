n=int(input("Enter any number: "))
l=[]
while n!=1 and n not in l:
    l.append(n)
    n=sum([int(i)*int(i) for i in str(n)])
if n==1:
    print("ROUND NUMBER")
else:
    print("NOT ROUND NUMBER")