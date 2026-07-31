# ==========================================
# Project: Employee Information System
# Topic: Python Lexical Structure
# ==========================================

# String Literal
company_name = "ABC Technologies"

# Integer Literal
employee_id = 101

# String Variable
employee_name = input("Enter Employee Name: ")

# Float Literal
salary = float(input("Enter Monthly Salary: "))

# Boolean
is_permanent = input("Permanent Employee? (yes/no): ").lower() == "yes"

# Arithmetic Operator
annual_salary = salary * 12

print("\n========== EMPLOYEE DETAILS ==========")
print("Company Name :", company_name)
print("Employee ID  :", employee_id)
print("Employee Name:", employee_name)
print("Monthly Salary:", salary)
print("Annual Salary :", annual_salary)
print("Permanent Employee:", is_permanent)

# Conditional Statement
if is_permanent:
    print("Bonus Eligible: Yes")
else:
    print("Bonus Eligible: No")

print("======================================")