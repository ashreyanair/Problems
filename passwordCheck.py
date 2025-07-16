s=input("Enter the string")
dg=0
sc=0
up=0
lw=0
if(len(s)>7):
    for i in s:
        if(i.isupper()):
            up=up+1
        elif(i.islower()):
            lw=lw+1
        elif(i.isdigit()):
            dg=dg+1
        else:
            sc=sc+1
    if(up>0 and lw>0 and dg>0 and sc>0):
        print("GOOD PASSWORD")
    else:
        print("BAD PASSWORD")
else:
    print("BAD PASSWORD DUE TO LESS CHARACTERS")
