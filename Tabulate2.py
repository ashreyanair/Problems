from tabulate import tabulate
headers=["name","age","department"]
data=[
    ["Ravi",25,"HR"],
    ["Anjali",30,"Finance"],
    ["Mohan",28,"IT"],
    ["Sneha",26,"marketting"],
    ["Arun",32,"logistics"]
]
print(f"{headers[0]:<12}{headers[1]:<5}{headers[2]:<15}")
print("*" * 30)

for row in data:
    print(f"{row[0]:<12}{row[1]:<5}{row[2]:<15}")
    print("-" * 30)