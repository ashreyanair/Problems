from datetime import datetime
a=input("Enter the first date (YYYY-MM-DD): ")
b=input("Enter the second date (YYYY-MM-DD): ")
d1=datetime.strptime(a,"%Y-%m-%d")
d2=datetime.strptime(b,"%Y-%m-%d")
diff=d2-d1
print("Difference: ",abs(diff.days),"days")