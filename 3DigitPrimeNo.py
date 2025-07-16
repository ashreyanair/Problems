for i in range(100,1000):
    count=0
    for j in range(2,i):
        if(i%j==0):
            count=count+1
    if(count==0):
        count=count+1
        if(count<20):
            print(i,end=" ")

