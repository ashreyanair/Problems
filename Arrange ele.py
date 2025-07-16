a=[10,11,"Zakir","Bala",123,44,53,"Anuj",20,46,7,"Jack"]
odd=[]
even=[]
strings=[]
for i in a:
    if (type(i) == str):
        strings.append(i)
    elif(i%2==0):
        even.append(i)
    elif(i%2==1):
        odd.append(i)
even.sort()
odd.sort()
strings.sort()
print(even, odd, strings)

