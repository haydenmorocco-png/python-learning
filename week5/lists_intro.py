all_fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(f"All fruits: {all_fruits}")
print(f"First fruit: {all_fruits[0]}")
print(f"Last fruit: {all_fruits[-1]}")
print(f"First three: {all_fruits[0:3]}")
print(f"Last two: {all_fruits[-2:]}")
print(f"Reversed: {all_fruits[::-1]}")
all_fruits.append("fig")
print(f"After append: {all_fruits}")
all_fruits.insert(2,"blueberry")
print(f"After insert at index 2: {all_fruits}")
all_fruits.remove("date")
print(f"After remove 'date': {all_fruits}")
all_fruits.pop()
print(f"Popped: {all_fruits}")
all_fruits.sort()
print(f"Sorted: {all_fruits}")

numbers = [34, 17, 89, 42, 56, 23, 71, 8, 95, 61]
print(f"lenght: {len(numbers)} Sum: {sum(numbers)} Min: {min(numbers)} Max: {max(numbers)} Average: {sum(numbers) / len(numbers)}")
guess = int(input("Enter a number to search for: "))
if guess in numbers:
    print(f"{guess} is in the list at index {numbers.index(guess)}")
else:
    print(f"{guess} is not in the list.")

