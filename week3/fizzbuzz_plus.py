
number = 1
for number in range(1, 31):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

multiples = 0
for number in range(1, 1001):
    if number % 3 == 0 or number % 5 == 0:
        multiples += number
print(f"Sum of all multiples of 3 or 5 below 1001: {multiples}")
i = 0
number = 1
for number in range(1, 100):
    if number % 3 == 0 and number % 5 == 0:
        i += 1
print(f"FizzBuzz numbers between 1 and 100: {i}")
