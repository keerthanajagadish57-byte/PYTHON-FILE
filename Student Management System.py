students = []

# Getting details of 10 students
for i in range(10):
    print("\nStudent", i + 1)

    name = input("Enter name: ")
    department = input("Enter department: ")
    mark = int(input("Enter mark: "))

    students.append([name, department, mark])

# Display all students
print("\n--- STUDENT DETAILS ---")

for student in students:
    print("Name:", student[0])
    print("Department:", student[1])
    print("Mark:", student[2])
    print()

# Calculate average
total = 0

for student in students:
    total = total + student[2]

average = total / 10

print("Average Mark:", average)

# Find highest mark
highest = students[0]

for student in students:
    if student[2] > highest[2]:
        highest = student

print("\nHighest Mark Student:")
print("Name:", highest[0])
print("Department:", highest[1])
print("Mark:", highest[2])
