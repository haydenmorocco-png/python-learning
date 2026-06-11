contacts = {
    'alice johnson' : ('555-0101' , 'alice@example.com'),
    'bob kumar' : ('555-0102', 'bob@example.com'),
    'charlie diaz' : ('555-0103', 'charlie@example.com')
}

def show_menu():   
    print("=== Contacts ===")
    print("1. Add contact")
    print("2. Find contact")
    print("3. List all")
    print("4. Delete contact")
    print("5. Quit")
    while True:
        choice = input("Enter choice (1-5): ")
        try:
            r_choice = int(choice)
            if 1 <= r_choice <= 5:
                return r_choice
            else:
                print("Enter valid input.")
        except ValueError:
            print("Enter valid input.")

def add_contact(contacts):
    name = input("What's their name: ")
    number = input("What's their number: ")
    email = input("What's their email: ")
    contacts[name.lower()] = (number, email)
    return contacts

def find_contact(contacts):
    name = input("Search name: ")
    if name.lower() in contacts:
        print(f'Name : {name.title()}')
        print(f'Number: {contacts[name.lower()][0]}')
        print(f'Email: {contacts[name.lower()][1]}')
    else:
        print("Contact not found.")
    return

def list_all(contacts):
    for name in sorted(contacts):
        print(f'Name : {name.title()}')
        print(f'Number: {contacts[name][0]}')
        print(f'Email: {contacts[name][1]}')
        print()
    return

def delete_contact(contacts):
    delete_person = input("Delete which contact: ")
    if delete_person.lower() in contacts:
        del contacts[delete_person.lower()]
        print(f"{delete_person}'s contact has been deleted.")
    else:
        print("Contact not found.")
    return contacts

def main(contacts):
    while True:
        choice = show_menu()
        if choice == 1:
            contacts = add_contact(contacts)
        elif choice == 2:
            find_contact(contacts)
        elif choice == 3:
            list_all(contacts)
        elif choice == 4:
            delete_contact(contacts)
        elif choice == 5:
            break

main(contacts)



