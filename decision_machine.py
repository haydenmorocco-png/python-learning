print("=== Programming Language Recommender ===")
print()
print("Answer a few questions and I'll recommend a language.")
print()
print("Whats your main goal?")
print(" 1. AI/Data science")
print(" 2. Web Development")
print(" 3. Mobile apps")
print(" 4. General Programming")
answer = int(input("Enter 1-4: "))
experince = input("Do you have any coding experince? (yes/no):")
print()
print("--- Recommendation ---")
if answer == 1 or answer == 4:
    print("Recommended: Python")
elif answer == 2:
    if experince.lower() == "yes":
        print("Recommended: JavaScript + React")
    else:
        print("Recommended: HTML/CSS → JavaScript")
elif answer == 3:
    print("Recommended: Swift or Kotlin")
else:
    print("Error, try again.")
