notorious=["Darshan","Anuj","Rohit"]
names=["Anu","Darshan","Rohit","Jack","Priya","Bala","Rai","Ram","Raj","Benscore"]
score=[2,5,6,8,3,5,6,9,8,2]
for i in range(len(names)):
    if score[i]-5:
        if names[i] not in notorious:
            print(names[i])