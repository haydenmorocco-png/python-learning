def show_menu():   
    print("=== Unit Converter ===")
    print()
    print("1. Miles → Kilometers")
    print("2. Kilograms → Pounds")
    print("3. Liters → Gallons")
    print("4. Quit")
    print()
    while True:
        choice = input("Enter choice (1-4): ")
        try:
            r_choice = int(choice)
            if 1 <= r_choice <= 4:
                return r_choice
            else:
                print("Enter valid input.")
        except ValueError:
            print("Enter valid input.")

def miles_to_kilometers():
    while True:
        miles = input("Enter miles: ")
        try:
            r_miles = float(miles)
            print(f"{r_miles} mi = {(r_miles * 1.609344):.2f} km")
            print()
            return
        except ValueError:
            print("Enter a valid input.")

def kilos_to_pounds():
    while True:
        kilos = input("Enter kilograms: ")
        try:
            r_kilos = float(kilos)
            print(f"{r_kilos} kgs = {(r_kilos * 2.20462262):.2f} lbs")
            print()
            return
        except ValueError:
            print("Enter a valid input.")

def liters_to_gallons():
    while True:
        liters = input("Enter liters: ")
        try:
            r_liters = float(liters)
            print(f"{r_liters} L = {(r_liters / 3.78541178):.2f} gal")
            print()
            return
        except ValueError:
            print("Enter a valid input.")

def main():
    while True:
        choice = show_menu()
        if choice == 1:
            miles_to_kilometers()
        elif choice == 2:
            kilos_to_pounds()
        elif choice == 3:
            liters_to_gallons()
        else:
            print("Goodbye!")
            break

main()

