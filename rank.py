students = []
percentages = []


for i in range(5):
    name = input("Enter name of student " + str(i + 1) + ": ")
    students.append(name.upper())

    total = 0
    print("Enter marks for 3 subjects:")
    for j in range(3):
        mark = int(input(f"Subject {j + 1} marks: "))
        total += mark

    percentage = round((total / 300) * 100)
    percentages.append(percentage)


print("\nResults:")
for i in range(5):
    print(f"{i + 1}. {students[i]}: {percentages[i]}%")