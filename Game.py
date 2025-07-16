import random
n1=input("enter player 1 ")
n2=input("enter player 2 ")
print("guess number from 1 to 10 ")
nums=[]
while(len(nums)<=5):
    d=random.randint(1,10)
    if d not in nums:
        nums.append(d)

s1=0
s2=0
p1=[]
p2=[]
for i in range(3):
    print(f"ROUND {i+1}")
    print("{} guess ur choice ".format(n1))
    ch=int(input())
    while (ch in p1 or ch in p2):
        ch = int(input("it is taken choose another"))
    p1.append(ch)

    if ch in nums:
        print("CORRECT!")
        s1+=1
    else:
        print("WRONG!")

    print("{} guess ur choice ".format(n2))
    ch = int(input())
    while (ch in p1 or ch in p2):
        ch = int(input("it is taken choose another"))
    p2.append(ch)

    if ch in nums:
        print("CORRECT!")
        s2 += 1
    else:
        print("WRONG!")


print("GAME OVER ")
print("HIDDEN NUMBERS ARE {}".format(nums))
print("{} chose {}".format(n1,p1))
print("{} score is {}".format(n1,s1))
print("{} chose {}".format(n2,p2))
print("{} score is {}".format(n2,s2))
if s1>s2:
    print("The winner is {}".format(n1))
elif s2>s1:
    print("the winner is {}".format(n2))
else:
    print("draw")




