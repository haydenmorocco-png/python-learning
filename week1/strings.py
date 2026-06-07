name = input("What is your name? ")
fav_number = input("What is your favortie number? ")

number = int(fav_number)

print(f"Hello, {name}!")
print(f"Your name has {len(name)} letters")
print(f"Your name in all caps is {name.upper()}")
print(f"Your favortie number doubled is {number * 2}")
print(f"Your favorite number squared is {number **2}")

if ("a" in name.lower()) or ("e" in name.lower()):
    print("Your name has an a or e")
else:
    print("Your name doesnt have an a or e")
