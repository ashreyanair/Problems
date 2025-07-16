amount = int(input("Enter the amount: "))
denominations = [100, 500, 200, 50, 10, 20]
denominations.sort(reverse=True)

result = []

for i in denominations:
    while amount >= i:
        result.append(i)
        amount -= i

print("Denominations used:")
for note in result:
    print(note, end=", ")