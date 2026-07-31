print("===== Student Grade Calculator =====")

name = input("Enter Student Name: ")

marks = []

for i in range(1, 6):
    mark = float(input(f"Enter Marks for Subject {i}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 35:
    grade = "Pass"
else:
    grade = "Fail"

print("\n===== REPORT =====")
print("Name:", name)
print("Total:", total)
print("Percentage:", round(percentage, 2))
print("Grade:", grade)