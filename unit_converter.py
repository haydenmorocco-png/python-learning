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
            if 1 <= choice <= 4:
                return choice
            else:
                print("Enter a valid input.")
        except ValueError:
            print("Enter a valid input.")
            pass

num = show_menu()
print(num)


