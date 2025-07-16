a=int(input("Enter number of rows: "))
for i in range(a):
    for j in range(a-i-1):
        print(" ", end=" ")
    for k in range (i+1):
        print("* ",end=" ")
    print()