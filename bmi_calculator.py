print("=== BMI Calculator ===")
print()
metric = input("Use metric (kg/cm) or imperial (lb/in)? Enter 'm' or 'i': ")
if metric.lower() == "m" or metric.lower() == "i":
    if metric.lower() == "m":
        weight = float(input("Weight in kg: "))
        height = float(input("Height in cm: "))
        bmi = float(weight / ((height/100) ** 2))
    else:
        weight = float(input("Weight in lb: "))
        height = float(input("Height in in: "))
        bmi = float((weight / (height ** 2)) * 703)
else:
    print("Error, try again.")
    exit()
print()
print(f"Your BMI: {bmi:.1f}")
if bmi >= 30:
    print("Category: Obese")
elif bmi >= 25:
    print("Category: Overweight")
elif bmi >= 18.5:
    print("Category: Normal")
else:
    print("Category: Underweight")
print("(BMI is a rough estimate and not a medical diagnosis.)")