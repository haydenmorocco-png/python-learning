print("=== Tip Calculator ===")
bill_total = float(input("Enter the bill total ($):"))
tip_perecent = float(input("Enter tip % (e.g. 18 for 18%): "))
num_of_people = int(input("How many people are splitting the bill? "))

tp = tip_perecent / 100
tip_total = bill_total * tp 
total = tip_total + bill_total
per_person = total / num_of_people

print()
print(f"Bill total: ${bill_total:.2f}")
print(f"Tip {tip_perecent}%:  ${tip_total:.2f}")
print(f"Total:      ${total:.2f}")
print(f"Per person: ${per_person:.2f}")

