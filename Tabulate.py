from tabulate import tabulate
headers=["name","age","department"]
data=[
    ["Ravi",25,"HR"],
    ["Anjali",30,"Finance"],
    ["Mohan",28,"IT"],
    ["Sneha",26,"marketting"],
    ["Arun",32,"logistics"]
]
print(tabulate(data,headers=headers,tablefmt="fancy_grid"))