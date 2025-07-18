
def prime(i):
        if(i==1):
            return False
        else:
            for j in range(2,i):
                if(i%j==0):
                    return False
            return True
def sod(i):
    d=list(str(i))
    x=sum([int(i) for i in d])
    if(prime(x)):
        return True
    else:
        return False
def dig(i):
    while(i>0):
        d=i%10
        i=i//10
        if(not prime(d)):
            return False
    return True

for i in range(100,1000):
    if(prime(i) and sod(i) and dig(i)):
        print(i,end=" ")





























