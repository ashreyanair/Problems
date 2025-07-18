from readline import append_history_file

names=["A","B","C","D","E","F","G","H","I","J"]
memo=[0,1,1,1,2,2,1,2,1,2]
salary=[1000,1000,3000,4500,2000,5000,1500,2500,1300,1100]
data=zip(salary,memo,names)
removed1=[]
removed2=[]
for i in data:
    if i[0]>4000:
        removed1.append(i)
    print(removed1)

remaining=[i  for i in data if i(0) < 4000]
print(remaining)
a=sorted(remaining, key=lambda x:x[0],reverse=True)
for i in a:
    if(i[1]>=2):
        removed2.append(i)
    if(len(removed2)>3):
        break
final=removed1+removed2
ind=1
for i in final:
    print("{}.{} : Memo {}: Salary{}".format(ind,i[2],i[1],i[0]))
    ind=ind+1


