b=int(input("Enter the number of blocks: " ))
l=int(input("Enter the number of lines: " ))
s=int(input("Enter the number of stars: " ))
sum=0
print("------------------------")
for i in range(b):
    print("*--------{i+3}------------*")
    count=0
    for j in range(l-i):
        for k in range(s):
            print("*",end=" ")
            count=count+1
        print()
    print(count)
    sum+=count
print(sum)




