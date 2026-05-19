i = 1
print("Counting with while:")
while i <= 5:
    print(i)
    i += 1
print()
print("--- Password Gate ---")
password = "Clemson"
i = 1
while i <= 3:
    guess = input(f"Enter password (attempt {i}/3):")
    if password == guess:
        print("Access granted!")
        break
    else:
        print(f"Wrong password. {3 - i} attempt(s) remaining.")
        i += 1
else:
    print("Too many failed attempts. Account locked")
