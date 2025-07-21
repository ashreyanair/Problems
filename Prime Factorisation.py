def prime_factor(n):
    if n==1:
        return
    i=2
    while(n%i !=0):
        i=i+1
    print(i,end=" ")
    prime_factor(n//i)

n=int(input("Enter the number: "))
prime_factor(n)



