students = [
    {"name": "raju", "dept": "cse", "marks": [20, 30, 40]},
    {"name": "vijay", "dept": "cse", "marks": [10, 70, 43]},
    {"name": "pavi", "dept": "ece", "marks": [22, 38, 56]},
    {"name": "rose", "dept": "ece", "marks": [26, 36, 89]},
    {"name": "virat", "dept": "ece", "marks": [16, 90, 43]}
]
for i in students:
    sum1=sum(i["marks"])
    per=sum1//3
    i["per"]=per

des=["First","Second","Third","Fourth","Fifth"]
b=sorted(students,key=lambda x:x["per"],reverse=True)
index=1
for i in b:
    print("{}.{} stands {}:{}%".format(index,i["name"],des[index-1],i["per"]))
    index+=1

