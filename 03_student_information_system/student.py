print("===================================")
print("   STUDENT INFORMATION SYSTEM")
print("===================================\n")

name = input("Enter Student Name: ")
age = int(input("Enter Age: "))

marks = []

subjects = ("Python", "Math", "English")

for subject in subjects:
    mark = float(input(f"Enter {subject} Marks: "))
    marks.append(mark)

average = sum(marks) / len(marks)
passed = average >= 35

student = {
    "Name": name,
    "Age": age,
    "Subjects": subjects,
    "Marks": marks,
    "Average": average,
    "Passed": passed
}

print("\n===== STUDENT REPORT =====")
print("Name:", student["Name"])
print("Age:", student["Age"])
print("Subjects:", student["Subjects"])
print("Marks:", student["Marks"])
print("Average:", round(student["Average"], 2))
print("Passed:", student["Passed"])