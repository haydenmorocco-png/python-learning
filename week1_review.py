name = input("Enter your full name:")
birth_year = int(input("Enter your birth year:"))
hometown = input("Enter your hometown:")
fav_subject = input("Enter your favortie subject:")

age = 2026 - birth_year

print()
print("=============================")
print("     Personal Info Card      ")
print("=============================")
print(f"Name:         {name.title()}")
print(f"Age:          {age} years old ")
print(f"Hometown:     {hometown.title()}")
print(f"Fav subject:  {fav_subject.capitalize()}")
print(f"Initals:      {name[0].capitalize()}.{name[(name.index(" ") + 1)].capitalize()}")
print("=============================")