heads=int(input("Enter thr number of heads"))
legs=int(input("Enter thr number of legs"))
flag=False
for hens in range(heads):
    cows=heads-hens
    if(cows*4 + hens*2 == legs):
        print("Cows: ",cows)
        print("Hens: ", hens)
        flag=True
        break
if(not flag):
    print("No Solution")
