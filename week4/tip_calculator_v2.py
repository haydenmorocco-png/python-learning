def bill_input():
    bill_total = "A"
    try:
        bill_total = float(input("Enter the bill total ($):"))
    except ValueError:
        print("Please enter a valid number")
        return bill_input()
    return bill_total

def tip_input():
    tip_percent = "A"
    try:
        tip_percent = float(input("Enter tip % (e.g. 18 for 18%): "))
    except ValueError:
        print("Please enter a valid number")
        return tip_input()
    return tip_percent

def person_input():
    num_of_people = "A"
    try:
        num_of_people = int(input("How many people are splitting the bill? "))
    except ValueError:
        print("Please enter a valid number")
        return person_input()
    return num_of_people

def tip_amount(bill, tp):
    tip_total = bill * (tp / 100)
    return tip_total

def bill_total(bill, tip_total):
    bill_total = bill + tip_total
    return bill_total

def per_person_total(real_total, num_of_pep):
    per_person = real_total / num_of_pep
    return per_person

def receipt(total, bill_total, tip_total, tip_perecent, per_person):
    print()
    print(f"Bill total: ${bill_total:.2f}")
    print(f"Tip {tip_perecent}%:  ${tip_total:.2f}")
    print(f"Total:      ${total:.2f}")
    print(f"Per person: ${per_person:.2f}")

def main():
    print("=== Tip Calculator ===")
    og_bill = bill_input()
    tip = tip_input()
    people = person_input()
    tip_total = tip_amount(og_bill, tip)
    real_bill = bill_total(og_bill, tip_total)
    per_person = per_person_total(real_bill, people)
    receipt(real_bill, og_bill, tip_total, tip, per_person)

main()