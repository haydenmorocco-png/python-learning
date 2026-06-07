print("=== Eligibility Checker ===")
print()
gpa = float(input("Enter your GPA (0.0 - 4.0): "))
credit_hours = int(input("Enter completed credit hours: "))
student = str(input("are you a full-time student? (yes/no): "))
academic_violation = str(input("Do you have any academic violations? (yes/no): "))
print("--- Results ---")
if gpa >= 3.5 and student.lower() == "yes" and academic_violation.lower() == "no":
    print("Merit Scholarship: Eligible")
else:
    print("Merit Scholarship: Not Eligible")
if gpa >= 3.7 and credit_hours >= 30:
    print("Honor Society: Eligible")
else:
    print("Honor Society: Not Eligible")
if academic_violation.lower() == "no":
    print("AI Club: Eligible")
else:
    print("AI Club: Not Eligible")

