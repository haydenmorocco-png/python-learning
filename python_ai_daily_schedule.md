# Python & AI Daily Schedule — May 12 to August 15
> Every session = 60 minutes. Every day has exact tasks, timestamps, code prompts, and commit messages.
> Sources: **CS50P** = CS50's Intro to Python on edX | **FCC** = freeCodeCamp "Python for Beginners" on YouTube

---

## PHASE 1 — Python Foundations (Weeks 1–4)
### Goal: Variables → Functions → First project on GitHub

---

## WEEK 1 — Environment, Variables, and Your First Programs

---

### Monday, May 12
**Theme: Install everything. Run your first program.**

**Minutes 0–30: Setup**
1. Download and install Python 3.12 from https://python.org/downloads
2. Download and install VS Code from https://code.visualstudio.com
3. Open VS Code → Extensions (left sidebar) → search "Python" → install the Microsoft Python extension
4. Watch FCC YouTube: **0:00 – 6:00** (introduction and what Python is)

**Minutes 30–50: Coding task**
Create a folder on your Desktop called `python-summer`.
Open VS Code → File → Open Folder → select `python-summer`.
Create a new file called `hello.py`.
Type this exactly (do not copy-paste):
```python
name = "Your Name"
print("Hello, my name is", name)
print("I am learning Python.")
print("Today is Day 1.")
```
Run it: open the VS Code terminal (Ctrl+` ) and type:
```
python hello.py
```
You should see three lines printed. If you get an error, read it carefully — errors tell you exactly what went wrong.

**Minutes 50–60: GitHub setup**
1. Go to https://github.com and create a free account
2. Download Git from https://git-scm.com/downloads and install it
3. In your VS Code terminal, run these commands one by one:
```
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```
Write in your file `hello.py` at the bottom as a comment:
```python
# Day 1 complete. I set up Python, VS Code, and Git.
```
Save the file. You'll push to GitHub tomorrow once the repo is created.

---

### Tuesday, May 13
**Theme: Variables and data types**

**Minutes 0–30: Watch**
FCC YouTube: **6:00 – 22:00**
Topics covered: variables, strings, integers, floats, booleans
While watching: every time they type something, pause and type it yourself in a new file called `variables.py`

**Minutes 30–50: Coding task**
In `variables.py`, write a program that stores and prints the following (use your own real or made-up values):
```python
# Variables practice
first_name = "Alex"
last_name = "Johnson"
age = 19
gpa = 3.7
is_student = True

print("Name:", first_name, last_name)
print("Age:", age)
print("GPA:", gpa)
print("Currently a student:", is_student)

# String operations
print("Full name uppercase:", first_name.upper() + " " + last_name.upper())
print("Name length:", len(first_name))
print("Greeting:", "Hello, my name is " + first_name + " and I am " + str(age) + " years old.")
```
Run it. Fix any errors. Make sure all 7 print statements produce output.

**Minutes 50–60: GitHub — create your repo**
Go to github.com → click the green "New" button → name the repo `python-learning` → check "Add a README file" → click "Create repository".
Back in VS Code terminal:
```
cd ~/Desktop/python-summer
git init
git remote add origin https://github.com/YOURUSERNAME/python-learning.git
git add .
git commit -m "Add Day 1 hello.py and Day 2 variables practice"
git push -u origin main
```
If it asks for your GitHub password, use a Personal Access Token (Settings → Developer settings → Tokens on GitHub).

---

### Wednesday, May 14
**Theme: String methods and f-strings**

**Minutes 0–30: Watch**
FCC YouTube: **22:00 – 36:00**
Topics: string methods, f-strings, type conversion
Pause and type every example in a new file called `strings.py`

**Minutes 30–50: Coding task**
In `strings.py`, write a program that asks the user for their name and favorite number, then prints a personalized message:
```python
# String methods and f-strings
name = input("What is your name? ")
favorite_number = input("What is your favorite number? ")

# Convert to integer so we can do math
number = int(favorite_number)

print(f"Hello, {name}!")
print(f"Your name has {len(name)} letters.")
print(f"Your name in all caps: {name.upper()}")
print(f"Your favorite number doubled is {number * 2}.")
print(f"Your favorite number squared is {number ** 2}.")

# Check if the name contains a vowel
if "a" in name.lower() or "e" in name.lower():
    print(f"Your name contains the letter A or E.")
else:
    print(f"Your name does not contain A or E.")
```
Run it. Test it with different inputs including a number like 7.

**Minutes 50–60: Commit**
```
git add strings.py
git commit -m "Add string methods and f-string practice with user input"
git push
```

---

### Thursday, May 15
**Theme: Arithmetic, math operations, and a real program**

**Minutes 0–30: Watch**
FCC YouTube: **36:00 – 50:00**
Topics: arithmetic operators, math module, order of operations

**Minutes 30–50: Coding task**
Create `tip_calculator.py`. Build a tip calculator that:
- Asks for the bill total
- Asks for the tip percentage (e.g., 18)
- Asks how many people are splitting the bill
- Prints the tip amount, total bill, and each person's share

```python
# Tip Calculator
print("=== Tip Calculator ===")

bill = float(input("Enter the bill total ($): "))
tip_percent = float(input("Enter tip percentage (e.g. 18 for 18%): "))
num_people = int(input("How many people are splitting the bill? "))

tip_amount = bill * (tip_percent / 100)
total = bill + tip_amount
per_person = total / num_people

print(f"\nBill total:    ${bill:.2f}")
print(f"Tip ({tip_percent}%):     ${tip_amount:.2f}")
print(f"Total:         ${total:.2f}")
print(f"Per person:    ${per_person:.2f}")
```
Run it. Test with bill=$50, tip=20%, 3 people. Expected: $10 tip, $60 total, $20/person.

**Minutes 50–60: Commit**
```
git add tip_calculator.py
git commit -m "Add tip calculator with float input and formatted output"
git push
```

---

### Friday, May 16
**Theme: CS50P Lecture 0 — review and consolidate**

**Minutes 0–30: Watch**
CS50P on edX — open Lecture 0. Watch from **start to 28:00**.
Topics: `print()`, variables, user input, types
This covers the same ground you've done this week but from a different angle. You'll recognize things — that's the goal.

**Minutes 30–50: Coding task — Week 1 review program**
Create `week1_review.py`. Build a "personal info card" program from scratch without looking at previous files:
```python
# Personal Info Card — Week 1 Review
# Goal: Use everything from this week: variables, input(), f-strings, math, string methods

name = input("Enter your full name: ")
birth_year = int(input("Enter your birth year: "))
hometown = input("Enter your hometown: ")
fav_subject = input("Enter your favorite subject: ")

current_year = 2025
age = current_year - birth_year

print("\n=============================")
print("       PERSONAL INFO CARD    ")
print("=============================")
print(f"Name:       {name.title()}")
print(f"Age:        {age} years old")
print(f"Hometown:   {hometown.title()}")
print(f"Fav subject:{fav_subject}")
print(f"Initials:   {name[0].upper()}.{name.split()[-1][0].upper()}.")
print("=============================")
```
Run it. If `name.split()[-1][0]` confuses you, try printing just `name.split()` first to see what it produces.

**Minutes 50–60: README update and commit**
Open `README.md` in your `python-learning` repo on GitHub (click the pencil icon to edit) and write:
```
# Python Learning — Summer 2025

Documenting my daily Python practice as I prepare for an AI minor at Clemson.

## Week 1 — Completed
- hello.py: first program
- variables.py: data types and string methods
- strings.py: f-strings and user input
- tip_calculator.py: arithmetic and formatted output
- week1_review.py: end-of-week consolidation
```
Then commit locally:
```
git add week1_review.py README.md
git commit -m "Complete Week 1: variables, strings, arithmetic, f-strings"
git push
```

---

## WEEK 2 — Control Flow and Decisions

---

### Monday, May 19
**Theme: if / elif / else**

**Minutes 0–30: Watch**
FCC YouTube: **50:00 – 1:08:00**
Topics: comparison operators, if/elif/else
Type every example in a scratch file as you watch.

**Minutes 30–50: Coding task**
Create `grade_checker.py`:
```python
# Grade Checker
# Given a numerical score, print the letter grade and a message

score = int(input("Enter your exam score (0-100): "))

if score >= 90:
    grade = "A"
    message = "Excellent work!"
elif score >= 80:
    grade = "B"
    message = "Good job!"
elif score >= 70:
    grade = "C"
    message = "Passing, but room to improve."
elif score >= 60:
    grade = "D"
    message = "At risk. Consider getting a tutor."
else:
    grade = "F"
    message = "Did not pass. Let's talk about next steps."

print(f"\nScore: {score}/100")
print(f"Grade: {grade}")
print(f"Feedback: {message}")
```
Test it with scores: 95, 83, 72, 65, 45. Verify each produces the correct grade.

**Minutes 50–60: Commit**
```
git add grade_checker.py
git commit -m "Add grade checker using if/elif/else with 5 grade bands"
git push
```

---

### Tuesday, May 20
**Theme: Boolean logic — and, or, not**

**Minutes 0–30: Watch**
FCC YouTube: **1:08:00 – 1:22:00**
Topics: boolean operators, combining conditions, `not`

**Minutes 30–50: Coding task**
Create `eligibility_checker.py`:
```python
# Scholarship and Club Eligibility Checker

print("=== Eligibility Checker ===\n")

gpa = float(input("Enter your GPA (0.0 - 4.0): "))
credits = int(input("Enter completed credit hours: "))
is_full_time = input("Are you a full-time student? (yes/no): ").lower() == "yes"
has_violations = input("Do you have any academic violations? (yes/no): ").lower() == "yes"

# Merit scholarship: GPA >= 3.5 AND full-time AND no violations
merit_eligible = gpa >= 3.5 and is_full_time and not has_violations

# Honor society: GPA >= 3.7 AND at least 30 credits
honor_eligible = gpa >= 3.7 and credits >= 30

# AI club: Any GPA, just needs to be a student (always True here) and no violations
ai_club_eligible = not has_violations

print(f"\n--- Results ---")
print(f"Merit Scholarship: {'Eligible' if merit_eligible else 'Not eligible'}")
print(f"Honor Society:     {'Eligible' if honor_eligible else 'Not eligible'}")
print(f"AI Club:           {'Eligible' if ai_club_eligible else 'Not eligible'}")
```
Test it: GPA=3.8, 45 credits, full-time, no violations → should be eligible for all three.

**Minutes 50–60: Commit**
```
git add eligibility_checker.py
git commit -m "Add eligibility checker using boolean and/or/not logic"
git push
```

---

### Wednesday, May 21
**Theme: Nested conditionals and input validation**

**Minutes 0–30: Watch**
CS50P Lecture 0: **28:00 – 50:00**
Topics: conditionals, user input types, handling errors with try/except (just observe — you'll use this soon)

**Minutes 30–50: Coding task**
Create `bmi_calculator.py`:
```python
# BMI Calculator with nested conditionals

print("=== BMI Calculator ===\n")

unit = input("Use metric (kg/cm) or imperial (lb/in)? Enter 'm' or 'i': ").lower()

if unit == "m":
    weight = float(input("Weight in kg: "))
    height_cm = float(input("Height in cm: "))
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
elif unit == "i":
    weight = float(input("Weight in pounds: "))
    height_in = float(input("Height in inches: "))
    bmi = (weight / (height_in ** 2)) * 703
else:
    print("Invalid unit. Please enter 'm' or 'i'.")
    bmi = None

if bmi is not None:
    bmi = round(bmi, 1)
    print(f"\nYour BMI: {bmi}")
    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal weight")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")
    print("(BMI is a rough estimate and not a medical diagnosis.)")
```
Test: 70 kg, 175 cm → BMI ≈ 22.9, Normal weight.

**Minutes 50–60: Commit**
```
git add bmi_calculator.py
git commit -m "Add BMI calculator with metric/imperial input and nested conditionals"
git push
```

---

### Thursday, May 22
**Theme: CS50P Problem Set 0**

**Minutes 0–30: Watch**
CS50P Lecture 0: **50:00 – end**
Topics: `int()`, `float()`, `str()`, common bugs, reading error messages

**Minutes 30–50: CS50P Problem Set 0**
Go to CS50P on edX → Problem Set 0.
Complete **"Indoor Voice"**: accepts a line of text and prints it in lowercase.
```python
# indoor_voice.py
text = input()
print(text.lower())
```
Then complete **"Playback Speed"**: replaces spaces with `...`
```python
# playback_speed.py
text = input()
print(text.replace(" ", "..."))
```
Submit both on edX if you have an account, or just run them locally.

**Minutes 50–60: Commit**
```
git add indoor_voice.py playback_speed.py
git commit -m "Complete CS50P Problem Set 0: indoor voice and playback speed"
git push
```

---

### Friday, May 23
**Theme: Week 2 review + prep for loops**

**Minutes 0–30: Watch**
FCC YouTube: **1:22:00 – 1:38:00**
Topics: while loops (preview) — just watch, don't code yet. You're priming your brain for next week.

**Minutes 30–50: Coding task — Week 2 consolidation**
Create `decision_machine.py` — a simple quiz program using everything from Week 2:
```python
# Decision Machine — What programming language should you learn?

print("=== Programming Language Recommender ===\n")
print("Answer a few questions and I'll recommend a language.\n")

goal = input("What's your main goal?\n  1. AI/data science\n  2. Web development\n  3. Mobile apps\n  4. General programming\nEnter 1-4: ")

experience = input("\nDo you have any coding experience? (yes/no): ").lower()
likes_math = input("Do you enjoy math? (yes/no): ").lower()

goal = int(goal)
is_experienced = experience == "yes"
enjoys_math = likes_math == "yes"

print("\n--- Recommendation ---")

if goal == 1:
    print("Recommended: Python")
    print("Reason: Python dominates AI and data science.")
elif goal == 2:
    if is_experienced:
        print("Recommended: JavaScript + React")
    else:
        print("Recommended: HTML/CSS then JavaScript")
elif goal == 3:
    print("Recommended: Swift (iOS) or Kotlin (Android)")
elif goal == 4:
    if enjoys_math:
        print("Recommended: Python or Java")
    else:
        print("Recommended: Python — the most beginner-friendly.")
else:
    print("Invalid choice. Please re-run and enter 1-4.")
```

**Minutes 50–60: README update and commit**
Add to your README on GitHub:
```
## Week 2 — Completed
- grade_checker.py: if/elif/else with 5 grade bands
- eligibility_checker.py: boolean and/or/not logic
- bmi_calculator.py: nested conditionals, two unit systems
- CS50P Problem Set 0: indoor_voice.py, playback_speed.py
- decision_machine.py: week 2 review program
```
```
git add decision_machine.py README.md
git commit -m "Complete Week 2: conditionals, boolean logic, nested if, CS50P PS0"
git push
```

---

## WEEK 3 — Loops and Iteration

---

### Monday, May 26
**Theme: for loops and range()**

**Minutes 0–30: Watch**
FCC YouTube: **1:38:00 – 1:55:00**
Topics: for loops, range(), iterating over sequences

**Minutes 30–50: Coding task**
Create `loops_intro.py`:
```python
# For loop fundamentals

# 1. Count from 1 to 10
print("Counting to 10:")
for i in range(1, 11):
    print(i, end=" ")
print()  # new line

# 2. Print only even numbers 2-20
print("\nEven numbers 2-20:")
for i in range(2, 21, 2):
    print(i, end=" ")
print()

# 3. Countdown from 10 to 1
print("\nCountdown:")
for i in range(10, 0, -1):
    print(i, end=" ")
print("Blast off!")

# 4. Print a times table
number = int(input("\nEnter a number for its times table: "))
print(f"\nTimes table for {number}:")
for i in range(1, 13):
    print(f"  {number} x {i} = {number * i}")
```
Run it. Enter 7 for the times table. Verify 7x12=84.

**Minutes 50–60: Commit**
```
git add loops_intro.py
git commit -m "Add for loop fundamentals: range, step, countdown, times table"
git push
```

---

### Tuesday, May 27
**Theme: while loops and break**

**Minutes 0–30: Watch**
FCC YouTube: **1:55:00 – 2:12:00**
Topics: while loops, break, continue, infinite loops and how to avoid them

**Minutes 30–50: Coding task**
Create `while_loops.py`:
```python
# While loop fundamentals

# 1. Basic while loop — count to 5
count = 1
print("Counting with while:")
while count <= 5:
    print(count)
    count += 1  # CRITICAL: without this, infinite loop!

# 2. Password checker (loops until correct)
print("\n--- Password Gate ---")
correct_password = "clemson123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input(f"Enter password (attempt {attempts + 1}/{max_attempts}): ")
    attempts += 1
    if password == correct_password:
        print("Access granted!")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Wrong password. {remaining} attempt(s) remaining.")
else:
    print("Too many failed attempts. Account locked.")
```
Test it: enter the wrong password twice, then `clemson123`. Then test entering wrong 3 times.

**Minutes 50–60: Commit**
```
git add while_loops.py
git commit -m "Add while loop practice: counter and password gate with break"
git push
```

---

### Wednesday, May 28
**Theme: Nested loops**

**Minutes 0–30: Watch**
CS50P Lecture 1: **0:00 – 25:00** (on edX)
Topics: loops in depth, indentation rules, loop patterns

**Minutes 30–50: Coding task**
Create `nested_loops.py`:
```python
# Nested loops

# 1. Multiplication table grid (3x3)
print("Multiplication Table (1-5):\n")
print("   ", end="")
for i in range(1, 6):
    print(f"{i:4}", end="")
print()
print("   " + "----" * 5)
for i in range(1, 6):
    print(f"{i} |", end="")
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print()

# 2. Triangle pattern
print("\nStar triangle:")
rows = int(input("How many rows? "))
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

# 3. Number pyramid
print("\nNumber pyramid:")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```
Run it with rows=5. The triangle should be 5 rows of stars; the pyramid 1, 12, 123, etc.

**Minutes 50–60: Commit**
```
git add nested_loops.py
git commit -m "Add nested loops: multiplication table, star triangle, number pyramid"
git push
```

---

### Thursday, May 29
**Theme: Loop + conditionals combined**

**Minutes 0–30: Watch**
CS50P Lecture 1: **25:00 – 50:00**
Topics: combining loops with conditionals, modulo operator `%`, FizzBuzz

**Minutes 30–50: Coding task**
Create `fizzbuzz_plus.py`:
```python
# FizzBuzz — a classic programming interview problem

print("FizzBuzz (1-30):")
for i in range(1, 31):
    if i % 15 == 0:        # divisible by both 3 and 5
        print("FizzBuzz")
    elif i % 3 == 0:       # divisible by 3
        print("Fizz")
    elif i % 5 == 0:       # divisible by 5
        print("Buzz")
    else:
        print(i)

# Extended: sum of all numbers divisible by 3 OR 5, from 1 to 1000
total = 0
for i in range(1, 1001):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(f"\nSum of all multiples of 3 or 5 below 1001: {total}")
# Expected answer: 234168

# Count how many FizzBuzz numbers exist between 1 and 100
fb_count = sum(1 for i in range(1, 101) if i % 15 == 0)
print(f"FizzBuzz numbers between 1 and 100: {fb_count}")
# Expected: 6 (15, 30, 45, 60, 75, 90)
```

**Minutes 50–60: Commit**
```
git add fizzbuzz_plus.py
git commit -m "Add FizzBuzz with modulo operator, sum of multiples, and count"
git push
```

---

### Friday, May 30
**Theme: Mini-project — Number Guessing Game (Project 1)**

**Minutes 0–5: Review**
Re-read your `while_loops.py` and `fizzbuzz_plus.py`. You need: loops, conditionals, random numbers.

**Minutes 5–50: Build Project 1**
Create `guessing_game.py` in a new folder `projects/guessing-game/`:
```python
# Number Guessing Game — Project 1
# Skills: while loops, if/elif/else, random module, functions, input validation

import random

def play_game(difficulty):
    """Run one round of the guessing game. Returns number of guesses."""
    secret = random.randint(1, 100)
    
    if difficulty == "easy":
        max_guesses = 10
    elif difficulty == "hard":
        max_guesses = 5
    else:
        max_guesses = 7  # medium
    
    print(f"\nI've picked a number between 1 and 100.")
    print(f"You have {max_guesses} guesses. Good luck!\n")
    
    guesses_used = 0
    
    while guesses_used < max_guesses:
        guess_str = input(f"Guess {guesses_used + 1}/{max_guesses}: ")
        
        # Input validation
        if not guess_str.isdigit():
            print("Please enter a whole number.")
            continue
        
        guess = int(guess_str)
        guesses_used += 1
        
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            guesses_used -= 1  # don't count invalid guess
        elif guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"\nCORRECT! The number was {secret}.")
            print(f"You got it in {guesses_used} guess(es)!")
            return guesses_used
    
    print(f"\nOut of guesses! The number was {secret}.")
    return None  # None means player lost

def main():
    print("=================================")
    print("     NUMBER GUESSING GAME        ")
    print("=================================\n")
    
    wins = 0
    losses = 0
    
    while True:
        print(f"Score: {wins} wins, {losses} losses\n")
        
        difficulty = input("Choose difficulty — easy / medium / hard: ").lower()
        if difficulty not in ["easy", "medium", "hard"]:
            print("Invalid difficulty. Defaulting to medium.")
            difficulty = "medium"
        
        result = play_game(difficulty)
        
        if result is not None:
            wins += 1
        else:
            losses += 1
        
        again = input("\nPlay again? (yes/no): ").lower()
        if again != "yes":
            break
    
    print(f"\nFinal score: {wins} win(s), {losses} loss(es). See you next time!")

main()
```

**Minutes 50–60: Commit with proper project structure**
Create `projects/guessing-game/README.md`:
```markdown
# Number Guessing Game

A command-line guessing game where the computer picks a secret number (1–100) and the player guesses it.

## How to run
python guessing_game.py

## Features
- Three difficulty levels (easy: 10 guesses, medium: 7, hard: 5)
- Input validation (rejects non-numbers and out-of-range guesses)
- Win/loss tracking across multiple rounds

## Skills demonstrated
- while loops, if/elif/else, functions, random module, input validation

## What I learned
Functions let me reuse the game logic cleanly. The `random` module showed me Python's standard library.
```
```
git add projects/
git commit -m "Add Project 1: number guessing game with difficulty levels and input validation"
git push
```

---

## WEEK 4 — Functions in Depth

---

### Monday, Jun 2
**Theme: Functions — parameters and return values**

**Minutes 0–30: Watch**
FCC YouTube: **2:12:00 – 2:30:00**
Topics: defining functions, parameters, arguments, return values

**Minutes 30–50: Coding task**
Create `functions_intro.py`:
```python
# Function fundamentals

# 1. Function with no parameters
def greet():
    print("Hello! Welcome to Python.")

# 2. Function with a parameter
def greet_person(name):
    print(f"Hello, {name}! Welcome to Python.")

# 3. Function with multiple parameters
def add(a, b):
    return a + b

# 4. Function that returns a value we can use
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Calling them:
greet()
greet_person("Alex")

result = add(15, 27)
print(f"15 + 27 = {result}")

temp_c = 100
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

temp_f_input = 98.6
temp_c_result = fahrenheit_to_celsius(temp_f_input)
print(f"{temp_f_input}°F = {round(temp_c_result, 1)}°C")

# 5. Function calling another function
def describe_temp(celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    if celsius < 0:
        description = "freezing"
    elif celsius < 15:
        description = "cold"
    elif celsius < 25:
        description = "comfortable"
    else:
        description = "hot"
    return f"{celsius}°C ({fahrenheit}°F) — {description}"

for temp in [-10, 5, 20, 35]:
    print(describe_temp(temp))
```

**Minutes 50–60: Commit**
```
git add functions_intro.py
git commit -m "Add function fundamentals: parameters, return values, functions calling functions"
git push
```

---

### Tuesday, Jun 3
**Theme: Default parameters and multiple return values**

**Minutes 0–30: Watch**
CS50P Lecture 2: **0:00 – 25:00**
Topics: functions in depth, default values, `*args`

**Minutes 30–50: Coding task**
Create `functions_advanced.py`:
```python
# Advanced function patterns

# 1. Default parameter values
def make_coffee(size="medium", milk=True, shots=1):
    milk_str = "with milk" if milk else "black"
    return f"{size.title()} coffee, {shots} shot(s), {milk_str}"

print(make_coffee())                          # all defaults
print(make_coffee("large"))                   # override size
print(make_coffee("small", False, 2))         # override all
print(make_coffee(shots=3, milk=False))       # keyword args

# 2. Multiple return values
def get_stats(numbers):
    """Given a list of numbers, return min, max, and average."""
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average  # returns a tuple

scores = [88, 72, 95, 61, 83, 79, 91, 68]
low, high, avg = get_stats(scores)
print(f"\nTest scores: {scores}")
print(f"Lowest:  {low}")
print(f"Highest: {high}")
print(f"Average: {avg:.1f}")

# 3. Docstrings — always document your functions
def compound_interest(principal, rate, years):
    """
    Calculate compound interest.
    
    Args:
        principal: starting amount in dollars
        rate: annual interest rate as decimal (e.g. 0.05 for 5%)
        years: number of years
    
    Returns:
        Final amount after compound interest
    """
    return principal * (1 + rate) ** years

amount = compound_interest(1000, 0.07, 10)
print(f"\n$1000 at 7% for 10 years: ${amount:.2f}")
```

**Minutes 50–60: Commit**
```
git add functions_advanced.py
git commit -m "Add advanced functions: default params, multiple returns, docstrings"
git push
```

---

### Wednesday, Jun 4
**Theme: Scope and organizing code**

**Minutes 0–30: Watch**
CS50P Lecture 2: **25:00 – 50:00**
Topics: variable scope, global vs local, organizing code into functions

**Minutes 30–50: Coding task**
Refactor your tip calculator from Week 1. Create `tip_calculator_v2.py`:
```python
# Tip Calculator v2 — fully refactored with functions

def get_bill_amount():
    """Prompt user for bill amount and validate input."""
    while True:
        try:
            amount = float(input("Enter the bill total ($): "))
            if amount <= 0:
                print("Bill must be greater than $0.")
            else:
                return amount
        except ValueError:
            print("Please enter a valid number.")

def calculate_tip(bill, percentage):
    """Calculate tip amount from bill and tip percentage."""
    return bill * (percentage / 100)

def split_bill(total, num_people):
    """Calculate each person's share."""
    return total / num_people

def print_summary(bill, tip_pct, num_people):
    """Print the full bill summary."""
    tip = calculate_tip(bill, tip_pct)
    total = bill + tip
    per_person = split_bill(total, num_people)
    
    print("\n" + "="*30)
    print("       BILL SUMMARY")
    print("="*30)
    print(f"  Bill total:     ${bill:.2f}")
    print(f"  Tip ({tip_pct}%):       ${tip:.2f}")
    print(f"  Total:          ${total:.2f}")
    print(f"  People:         {num_people}")
    print(f"  Per person:     ${per_person:.2f}")
    print("="*30)

def main():
    print("=== Tip Calculator v2 ===\n")
    bill = get_bill_amount()
    tip_pct = float(input("Tip percentage (e.g. 18): "))
    num_people = int(input("Number of people splitting: "))
    print_summary(bill, tip_pct, num_people)

main()
```
Notice how every piece of logic is now in its own function. This is professional Python style.

**Minutes 50–60: Commit**
```
git add tip_calculator_v2.py
git commit -m "Refactor tip calculator into clean functions with input validation"
git push
```

---

### Thursday, Jun 5
**Theme: CS50P Problem Set 1**

**Minutes 0–30: Watch**
CS50P Lecture 2: **50:00 – end**

**Minutes 30–50: CS50P Problem Set 1**
Complete **"Deep Thought"** from CS50P PS1:
```python
# deep_thought.py
def main():
    answer = int(input("What is the Answer to the Great Question of Life, the Universe, and Everything? "))
    if answer == 42:
        print("Yes!")
    else:
        print("No.")
main()
```
Then complete **"Home Federal Savings Bank"** (greet differently based on the first word of input):
```python
# home_federal.py
def main():
    greeting = input("Greeting: ").strip().lower()
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")
main()
```
Test: "Hello, there" → $0. "How are you?" → $20. "What's up?" → $100.

**Minutes 50–60: Commit**
```
git add deep_thought.py home_federal.py
git commit -m "Complete CS50P Problem Set 1: deep_thought and home_federal"
git push
```

---

### Friday, Jun 6
**Theme: Phase 1 wrap-up and repo polish**

**Minutes 0–30: Watch**
FCC YouTube: **2:30:00 – 2:48:00**
Topics: recap of functions, quick intro to scope — preview of what's next

**Minutes 30–50: Coding task — week 4 capstone**
Create `unit_converter.py` using everything from weeks 1–4:
```python
# Unit Converter — Phase 1 Capstone Exercise
# Uses: functions, loops, conditionals, input validation, f-strings

def miles_to_km(miles):
    """Convert miles to kilometers."""
    return miles * 1.60934

def kg_to_lbs(kg):
    """Convert kilograms to pounds."""
    return kg * 2.20462

def liters_to_gallons(liters):
    """Convert liters to US gallons."""
    return liters * 0.264172

def show_menu():
    print("\n=== Unit Converter ===")
    print("1. Miles → Kilometers")
    print("2. Kilograms → Pounds")
    print("3. Liters → Gallons")
    print("4. Quit")

def main():
    while True:
        show_menu()
        choice = input("\nEnter choice (1-4): ")
        
        if choice == "1":
            miles = float(input("Enter miles: "))
            km = miles_to_km(miles)
            print(f"{miles} miles = {km:.2f} km")
        elif choice == "2":
            kg = float(input("Enter kilograms: "))
            lbs = kg_to_lbs(kg)
            print(f"{kg} kg = {lbs:.2f} lbs")
        elif choice == "3":
            liters = float(input("Enter liters: "))
            gallons = liters_to_gallons(liters)
            print(f"{liters} liters = {gallons:.3f} gallons")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

main()
```

**Minutes 50–60: Full Phase 1 commit and README update**
Update your README to add Week 4 entries. Then:
```
git add unit_converter.py README.md
git commit -m "Complete Phase 1: functions, loops, conditionals, input validation, two CS50P problem sets"
git push
```

---

## PHASE 2 — Data Structures and Logic (Weeks 5–8)
### Goal: Lists → Dicts → Files → NumPy

---

## WEEK 5 — Lists

---

### Monday, Jun 9
**Theme: Lists — creation, indexing, methods**

**Minutes 0–30: Watch**
FCC YouTube: **2:48:00 – 3:10:00**
Topics: lists, indexing, slicing, list methods

**Minutes 30–50: Coding task**
Create `lists_intro.py`:
```python
# List fundamentals

# 1. Creating and accessing lists
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("All fruits:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("First three:", fruits[:3])
print("Last two:", fruits[-2:])
print("Reversed:", fruits[::-1])

# 2. Common list methods
fruits.append("fig")
print("\nAfter append:", fruits)

fruits.insert(2, "blueberry")
print("After insert at index 2:", fruits)

fruits.remove("date")
print("After remove 'date':", fruits)

popped = fruits.pop()
print(f"Popped: {popped}, Remaining: {fruits}")

fruits.sort()
print("Sorted:", fruits)

# 3. List operations
numbers = [34, 17, 89, 42, 56, 23, 71, 8, 95, 61]
print(f"\nNumbers: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Average: {sum(numbers)/len(numbers):.1f}")

# 4. Check membership
target = int(input("\nEnter a number to search for: "))
if target in numbers:
    print(f"{target} is in the list at index {numbers.index(target)}")
else:
    print(f"{target} is not in the list")
```

**Minutes 50–60: Commit**
```
git add lists_intro.py
git commit -m "Add list fundamentals: indexing, slicing, methods, membership testing"
git push
```

---

### Tuesday, Jun 10
**Theme: List comprehensions**

**Minutes 0–30: Watch**
CS50P Lecture 3: **0:00 – 25:00**
Topics: exceptions and loops (also introduces list patterns)

**Minutes 30–50: Coding task**
Create `list_comprehensions.py`:
```python
# List comprehensions — a Python superpower

# 1. Basic comprehension: squares of 1-10
squares = [x**2 for x in range(1, 11)]
print("Squares:", squares)

# 2. Filtered comprehension: only even squares
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print("Even squares:", even_squares)

# 3. String comprehension
words = ["hello", "world", "python", "is", "great"]
uppercase = [word.upper() for word in words]
print("Uppercase:", uppercase)

long_words = [word for word in words if len(word) > 4]
print("Long words (>4 chars):", long_words)

# 4. Real-world use: cleaning a dataset
# Imagine you got temperatures with some bad data (negative values)
raw_temps = [72, -1, 68, 75, -5, 80, 71, 999, 69, 74]
valid_temps = [t for t in raw_temps if 0 <= t <= 120]
print(f"\nRaw temps: {raw_temps}")
print(f"Valid temps: {valid_temps}")
print(f"Average valid temp: {sum(valid_temps)/len(valid_temps):.1f}°F")

# 5. Transform comprehension: Fahrenheit to Celsius
fahrenheit = [32, 68, 86, 104, 212]
celsius = [round((f - 32) * 5/9, 1) for f in fahrenheit]
print(f"\nFahrenheit: {fahrenheit}")
print(f"Celsius:    {celsius}")
```

**Minutes 50–60: Commit**
```
git add list_comprehensions.py
git commit -m "Add list comprehensions: filtering, transforming, data cleaning"
git push
```

---

### Wednesday, Jun 11
**Theme: Sorting and working with lists of data**

**Minutes 0–30: Watch**
CS50P Lecture 3: **25:00 – 50:00**

**Minutes 30–50: Coding task**
Create `student_scores.py`:
```python
# Student score tracker — simulated gradebook

students = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 72},
    {"name": "Charlie", "score": 95},
    {"name": "Diana", "score": 61},
    {"name": "Eve", "score": 83},
    {"name": "Frank", "score": 79},
    {"name": "Grace", "score": 91},
    {"name": "Henry", "score": 68},
]

# Sort by score descending
ranked = sorted(students, key=lambda s: s["score"], reverse=True)

print("=== CLASS RANKINGS ===")
for i, student in enumerate(ranked, start=1):
    score = student["score"]
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "D/F"
    print(f"  {i}. {student['name']:<10} {score:3}  ({grade})")

scores = [s["score"] for s in students]
print(f"\nClass average: {sum(scores)/len(scores):.1f}")
print(f"Highest: {max(scores)}  |  Lowest: {min(scores)}")

above_avg = [s["name"] for s in students if s["score"] >= sum(scores)/len(scores)]
print(f"Above average: {', '.join(above_avg)}")
```

**Minutes 50–60: Commit**
```
git add student_scores.py
git commit -m "Add student score tracker with sorting, ranking, and grade calculation"
git push
```

---

### Thursday, Jun 12
**Theme: Lists with loops — real data patterns**

**Minutes 0–30: Watch**
FCC YouTube: **3:10:00 – 3:28:00**

**Minutes 30–50: Coding task**
Create `word_counter_v1.py`:
```python
# Word frequency counter — a foundational NLP technique
# This is literally how early text analysis worked

text = """
Python is a great programming language. Python is used for 
data science, web development, and artificial intelligence. 
Python is beginner friendly and Python has a huge community.
Many data scientists use Python every day.
"""

# Step 1: Clean and split into words
words = text.lower().split()
cleaned = []
for word in words:
    # Remove punctuation from each word
    clean_word = word.strip(".,!?;:")
    if clean_word:  # skip empty strings
        cleaned.append(clean_word)

# Step 2: Count occurrences using a dict approach (preview of Week 6)
frequency = {}
for word in cleaned:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Step 3: Sort by frequency
sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

print(f"Total words: {len(cleaned)}")
print(f"Unique words: {len(frequency)}")
print("\nTop 10 most frequent words:")
for word, count in sorted_words[:10]:
    bar = "█" * count
    print(f"  {word:<15} {count:2}  {bar}")
```

**Minutes 50–60: Commit**
```
git add word_counter_v1.py
git commit -m "Add word frequency counter using list operations and basic dict counting"
git push
```

---

### Friday, Jun 13
**Theme: Week 5 review + lists mini-challenge**

**Minutes 0–30: Watch**
CS50P Lecture 3: **50:00 – end**

**Minutes 30–50: Coding task**
Create `lotto_simulator.py`:
```python
# Lottery Simulator — uses random, lists, sorting, functions

import random

def generate_ticket():
    """Generate 6 unique random numbers between 1 and 49."""
    ticket = []
    while len(ticket) < 6:
        num = random.randint(1, 49)
        if num not in ticket:
            ticket.append(num)
    return sorted(ticket)

def check_ticket(ticket, winning_numbers):
    """Return the count of matching numbers."""
    matches = [num for num in ticket if num in winning_numbers]
    return len(matches), matches

def prize(matches):
    """Return prize amount based on matches."""
    prizes = {6: 1000000, 5: 1000, 4: 100, 3: 10, 2: 0, 1: 0, 0: 0}
    return prizes[matches]

# Simulate
winning = generate_ticket()
print(f"Winning numbers: {winning}")
print()

total_spent = 0
total_won = 0

for i in range(10):
    my_ticket = generate_ticket()
    num_matches, matched = check_ticket(my_ticket, winning)
    won = prize(num_matches)
    total_spent += 2  # $2 per ticket
    total_won += won
    print(f"Ticket {i+1}: {my_ticket}  →  {num_matches} match(es) {matched}  ${won}")

print(f"\nTotal spent: ${total_spent}")
print(f"Total won:   ${total_won}")
print(f"Net result:  ${total_won - total_spent}")
```

**Minutes 50–60: README + commit**
Add Week 5 to README:
```
## Week 5 — Completed
- lists_intro.py, list_comprehensions.py, student_scores.py
- word_counter_v1.py: foundational NLP technique
- lotto_simulator.py: random, lists, functions combined
```
```
git add lotto_simulator.py README.md
git commit -m "Complete Week 5: lists, comprehensions, sorting, word counting, simulation"
git push
```

---

## WEEK 6 — Dictionaries and Sets

---

### Monday, Jun 16
**Theme: Dictionaries**

**Minutes 0–30: Watch**
FCC YouTube: **3:28:00 – 3:48:00**
Topics: dictionaries, key-value pairs, methods

**Minutes 30–50: Coding task**
Create `dicts_intro.py`:
```python
# Dictionary fundamentals

# 1. Create and access
person = {
    "name": "Jordan Smith",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.6,
    "is_student": True
}

print("Name:", person["name"])
print("GPA:", person["gpa"])
print("Keys:", list(person.keys()))
print("Values:", list(person.values()))

# Safe access with .get() — won't crash if key missing
print("Minor:", person.get("minor", "Undeclared"))

# 2. Update and add entries
person["minor"] = "Artificial Intelligence"
person["gpa"] = 3.7  # update existing
print("\nUpdated person:", person)

# 3. Iterating a dictionary
print("\nAll info:")
for key, value in person.items():
    print(f"  {key}: {value}")

# 4. Dict of lists — a very common pattern
courses = {
    "CS101": ["Alice", "Bob", "Charlie"],
    "MATH201": ["Alice", "Diana", "Eve"],
    "AI301": ["Bob", "Charlie", "Diana", "Frank"]
}

# Find all students in AI courses
print("\nAI301 students:", courses["AI301"])
print("Number of AI301 students:", len(courses["AI301"]))

# Find which courses Alice is in
alice_courses = [course for course, students in courses.items() if "Alice" in students]
print("Alice's courses:", alice_courses)
```

**Minutes 50–60: Commit**
```
git add dicts_intro.py
git commit -m "Add dictionary fundamentals: CRUD, iteration, dict of lists"
git push
```

---

### Tuesday, Jun 17
**Theme: Word frequency counter (proper version)**

**Minutes 0–30: Watch**
CS50P Lecture 4: **0:00 – 25:00**
Topics: libraries, using modules, `collections`

**Minutes 30–50: Coding task**
Create `word_frequency.py` — this is your Word 6 project:
```python
# Word Frequency Counter — Project-quality version
# This is a real NLP preprocessing task

def clean_word(word):
    """Remove punctuation and convert to lowercase."""
    return word.lower().strip(".,!?;:\"'()-[]")

def count_words(text):
    """Return a dictionary of word frequencies."""
    words = text.split()
    frequency = {}
    for word in words:
        cleaned = clean_word(word)
        if cleaned and len(cleaned) > 1:  # skip empty and single-char
            frequency[cleaned] = frequency.get(cleaned, 0) + 1
    return frequency

def top_n_words(frequency, n=10):
    """Return the top n most frequent words."""
    return sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:n]

def print_report(frequency):
    """Print a formatted frequency report."""
    total = sum(frequency.values())
    unique = len(frequency)
    top = top_n_words(frequency, 15)
    
    print(f"Total words: {total}")
    print(f"Unique words: {unique}")
    print(f"\nTop 15 words:")
    print("-" * 35)
    for word, count in top:
        pct = count / total * 100
        bar = "█" * count
        print(f"  {word:<18} {count:3}  ({pct:.1f}%)")

# Test with a passage
sample_text = """
Artificial intelligence is transforming the world. Machine learning, 
a subset of artificial intelligence, enables computers to learn from data.
Deep learning, a subset of machine learning, uses neural networks.
Neural networks are inspired by the human brain. The human brain processes
information in parallel. Parallel processing makes neural networks powerful.
Data is the fuel for artificial intelligence. More data means better models.
Better models lead to better artificial intelligence systems.
"""

frequency = count_words(sample_text)
print_report(frequency)

# Save results to a file
with open("word_freq_output.txt", "w") as f:
    for word, count in sorted(frequency.items(), key=lambda x: x[1], reverse=True):
        f.write(f"{word}: {count}\n")
print("\nResults saved to word_freq_output.txt")
```

**Minutes 50–60: Commit**
```
git add word_frequency.py
git commit -m "Add word frequency counter: clean functions, formatted report, file output"
git push
```

---

### Wednesday, Jun 18
**Theme: Sets**

**Minutes 0–30: Watch**
FCC YouTube: **3:48:00 – 4:02:00**
Topics: sets, uniqueness, set operations

**Minutes 30–50: Coding task**
Create `sets_practice.py`:
```python
# Sets — uniqueness and set operations

# 1. Basic sets
colors = {"red", "blue", "green", "red", "blue"}  # duplicates removed automatically
print("Colors set:", colors)  # order not guaranteed
print("Number of unique colors:", len(colors))

# 2. Set operations
python_students = {"Alice", "Bob", "Charlie", "Diana", "Eve"}
java_students = {"Bob", "Diana", "Frank", "Grace", "Eve"}

# Who takes both? (intersection)
both = python_students & java_students
print(f"\nStudents in both courses: {both}")

# Who takes at least one? (union)
either = python_students | java_students
print(f"Students in either course: {either}")

# Who takes Python but NOT Java? (difference)
python_only = python_students - java_students
print(f"Python only: {python_only}")

# 3. Practical use: remove duplicates from a list while preserving uniqueness
raw_tags = ["python", "AI", "python", "machine learning", "AI", "python", "data"]
unique_tags = list(set(raw_tags))
print(f"\nRaw tags: {raw_tags}")
print(f"Unique tags: {sorted(unique_tags)}")

# 4. Set for fast membership testing (faster than list for large data)
valid_usernames = {"alice_j", "bob_k", "charlie_m", "diana_r"}
test_users = ["alice_j", "hacker_x", "bob_k", "unknown_user"]

for user in test_users:
    status = "VALID" if user in valid_usernames else "INVALID"
    print(f"  {user}: {status}")
```

**Minutes 50–60: Commit**
```
git add sets_practice.py
git commit -m "Add sets practice: uniqueness, union, intersection, difference, membership"
git push
```

---

### Thursday, Jun 19
**Theme: Dictionaries as data stores — contacts app**

**Minutes 0–30: Watch**
CS50P Lecture 4: **25:00 – 50:00**

**Minutes 30–50: Coding task**
Create `contacts.py`:
```python
# Simple Contacts Manager — using dicts as a database

contacts = {}

def add_contact(name, phone, email):
    contacts[name.lower()] = {"phone": phone, "email": email, "name": name}
    print(f"Added contact: {name}")

def find_contact(name):
    result = contacts.get(name.lower())
    if result:
        print(f"\n  Name:  {result['name']}")
        print(f"  Phone: {result['phone']}")
        print(f"  Email: {result['email']}")
    else:
        print(f"No contact found for '{name}'")

def list_all():
    if not contacts:
        print("No contacts saved.")
        return
    print(f"\n--- All Contacts ({len(contacts)}) ---")
    for key in sorted(contacts):
        c = contacts[key]
        print(f"  {c['name']:<20} {c['phone']}")

def delete_contact(name):
    if name.lower() in contacts:
        del contacts[name.lower()]
        print(f"Deleted: {name}")
    else:
        print(f"Contact '{name}' not found.")

# Pre-load some contacts
add_contact("Alice Johnson", "555-0101", "alice@example.com")
add_contact("Bob Kumar", "555-0102", "bob@example.com")
add_contact("Charlie Diaz", "555-0103", "charlie@example.com")

# Menu loop
while True:
    print("\n=== Contacts ===")
    print("1. Add contact")
    print("2. Find contact")
    print("3. List all")
    print("4. Delete contact")
    print("5. Quit")
    
    choice = input("Choice: ")
    if choice == "1":
        n = input("Name: ")
        p = input("Phone: ")
        e = input("Email: ")
        add_contact(n, p, e)
    elif choice == "2":
        find_contact(input("Search name: "))
    elif choice == "3":
        list_all()
    elif choice == "4":
        delete_contact(input("Name to delete: "))
    elif choice == "5":
        break
```

**Minutes 50–60: Commit**
```
git add contacts.py
git commit -m "Add contacts manager: CRUD operations using dictionaries as data store"
git push
```

---

### Friday, Jun 20
**Theme: Week 6 review**

**Minutes 0–30: Watch**
CS50P Lecture 4: **50:00 – end**

**Minutes 30–50: Coding task — combine lists, dicts, sets**
Create `inventory.py`:
```python
# Inventory Tracker — lists + dicts + sets combined

inventory = {
    "apple": {"price": 0.99, "quantity": 50, "category": "produce"},
    "bread": {"price": 2.49, "quantity": 30, "category": "bakery"},
    "milk": {"price": 3.79, "quantity": 20, "category": "dairy"},
    "cheese": {"price": 4.99, "quantity": 15, "category": "dairy"},
    "banana": {"price": 0.59, "quantity": 80, "category": "produce"},
    "yogurt": {"price": 1.29, "quantity": 25, "category": "dairy"},
}

# Total inventory value
total_value = sum(item["price"] * item["quantity"] for item in inventory.values())
print(f"Total inventory value: ${total_value:.2f}")

# Low stock alert (< 20 units)
low_stock = [name for name, item in inventory.items() if item["quantity"] < 20]
print(f"Low stock items: {low_stock}")

# Categories using a set
categories = {item["category"] for item in inventory.values()}
print(f"Categories: {categories}")

# Most expensive item
priciest = max(inventory.items(), key=lambda x: x[1]["price"])
print(f"Most expensive: {priciest[0]} at ${priciest[1]['price']}")

# Group by category
by_category = {}
for name, item in inventory.items():
    cat = item["category"]
    by_category.setdefault(cat, []).append(name)

print("\nBy category:")
for cat, items in sorted(by_category.items()):
    print(f"  {cat}: {', '.join(sorted(items))}")
```

**Minutes 50–60: README + commit**
```
git add inventory.py README.md
git commit -m "Complete Week 6: dicts, sets, word counter, contacts, inventory tracker"
git push
```

---

## WEEK 7 — File I/O and CSV

---

### Monday, Jun 23
**Theme: Reading and writing text files**

**Minutes 0–30: Watch**
FCC YouTube: **4:02:00 – 4:22:00**
Topics: file open/read/write, with statement, modes

**Minutes 30–50: Coding task**
Create `file_io.py`:
```python
# File reading and writing fundamentals

# 1. Write a file
print("Writing to file...")
with open("notes.txt", "w") as f:
    f.write("Day 1: Variables and data types\n")
    f.write("Day 2: Strings and f-strings\n")
    f.write("Day 3: Loops and iteration\n")
    f.write("Day 4: Functions\n")
    f.write("Day 5: Lists and dictionaries\n")
print("File written.")

# 2. Read the entire file
print("\nReading entire file:")
with open("notes.txt", "r") as f:
    content = f.read()
print(content)

# 3. Read line by line
print("Reading line by line:")
with open("notes.txt", "r") as f:
    for i, line in enumerate(f, start=1):
        print(f"  Line {i}: {line.strip()}")

# 4. Append to file (doesn't overwrite)
with open("notes.txt", "a") as f:
    f.write("Day 6: File I/O\n")

# 5. Read all lines into a list
with open("notes.txt", "r") as f:
    lines = f.readlines()
print(f"\nFile now has {len(lines)} lines.")

# 6. Search the file
search_term = "Functions"
matches = [line.strip() for line in lines if search_term.lower() in line.lower()]
print(f"\nLines containing '{search_term}':")
for match in matches:
    print(f"  {match}")
```

**Minutes 50–60: Commit**
```
git add file_io.py
git commit -m "Add file I/O fundamentals: read, write, append, search text files"
git push
```

---

### Tuesday, Jun 24
**Theme: CSV files — the bread and butter of data work**

**Minutes 0–30: Watch**
CS50P Lecture 6: **0:00 – 28:00**
Topics: file I/O, CSV module, reading structured data

**Minutes 30–50: Coding task**
First, create `students.csv` by running this:
```python
# create_sample_csv.py — run once to generate your data file
import csv

students = [
    ["Name", "Major", "GPA", "Year", "Scholarship"],
    ["Alice Johnson", "Computer Science", 3.8, "Junior", "Yes"],
    ["Bob Kumar", "Mathematics", 3.2, "Sophomore", "No"],
    ["Charlie Diaz", "Physics", 3.9, "Senior", "Yes"],
    ["Diana Lee", "Data Science", 3.6, "Junior", "Yes"],
    ["Eve Martin", "Computer Science", 2.9, "Freshman", "No"],
    ["Frank Zhao", "Statistics", 3.4, "Senior", "No"],
    ["Grace Kim", "AI", 3.7, "Junior", "Yes"],
    ["Henry Brown", "Math", 3.1, "Sophomore", "No"],
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)

print("students.csv created.")
```
Then create `csv_analysis.py`:
```python
# CSV analysis — reading and processing structured data
import csv

def load_students(filename):
    students = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["GPA"] = float(row["GPA"])  # convert string to float
            students.append(row)
    return students

students = load_students("students.csv")

print(f"Loaded {len(students)} students\n")

# Average GPA
avg_gpa = sum(s["GPA"] for s in students) / len(students)
print(f"Average GPA: {avg_gpa:.2f}")

# Top students (GPA >= 3.7)
top_students = [s for s in students if s["GPA"] >= 3.7]
print(f"\nTop students (GPA >= 3.7):")
for s in sorted(top_students, key=lambda x: x["GPA"], reverse=True):
    print(f"  {s['Name']:<20} {s['GPA']}  {s['Major']}")

# Count by major
majors = {}
for s in students:
    majors[s["Major"]] = majors.get(s["Major"], 0) + 1
print("\nStudents per major:")
for major, count in sorted(majors.items()):
    print(f"  {major}: {count}")

# Scholarship holders
scholars = [s["Name"] for s in students if s["Scholarship"] == "Yes"]
print(f"\nScholarship holders: {', '.join(scholars)}")
```

**Minutes 50–60: Commit**
```
git add create_sample_csv.py csv_analysis.py students.csv
git commit -m "Add CSV read/write with DictReader, filtering, grouping, and analysis"
git push
```

---

### Wednesday, Jun 25
**Theme: Working with a real-world dataset**

**Minutes 0–30: Setup**
Go to https://www.kaggle.com/datasets/yasserh/titanic-dataset and download `titanic.csv` (free account required) OR use this URL to download via Python:
```python
# download_titanic.py
import urllib.request
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
urllib.request.urlretrieve(url, "titanic.csv")
print("Downloaded titanic.csv")
```
Run that script. Then watch CS50P Lecture 6: **28:00 – 50:00**

**Minutes 30–50: Coding task**
Create `titanic_analysis.py`:
```python
# Titanic Dataset — first real-world data analysis
import csv

def load_titanic(filename):
    passengers = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert numeric columns
            try:
                row["Age"] = float(row["Age"]) if row["Age"] else None
                row["Fare"] = float(row["Fare"]) if row["Fare"] else None
                row["Survived"] = int(row["Survived"])
                row["Pclass"] = int(row["Pclass"])
            except:
                pass
            passengers.append(row)
    return passengers

passengers = load_titanic("titanic.csv")
print(f"Total passengers: {len(passengers)}\n")

# Overall survival rate
survivors = [p for p in passengers if p["Survived"] == 1]
print(f"Survival rate: {len(survivors)/len(passengers)*100:.1f}%")

# Survival by class
for pclass in [1, 2, 3]:
    class_p = [p for p in passengers if p["Pclass"] == pclass]
    class_s = [p for p in class_p if p["Survived"] == 1]
    print(f"Class {pclass}: {len(class_s)}/{len(class_p)} survived ({len(class_s)/len(class_p)*100:.1f}%)")

# Average age (ignore missing)
ages = [p["Age"] for p in passengers if p["Age"] is not None]
print(f"\nAverage age: {sum(ages)/len(ages):.1f}")

# Survival by gender
for sex in ["male", "female"]:
    group = [p for p in passengers if p["Sex"] == sex]
    survived = [p for p in group if p["Survived"] == 1]
    print(f"{sex.title()}: {len(survived)}/{len(group)} survived ({len(survived)/len(group)*100:.1f}%)")
```

**Minutes 50–60: Commit**
```
git add download_titanic.py titanic_analysis.py
git commit -m "Add Titanic CSV analysis: survival rates by class, gender, and age"
git push
```

---

### Thursday, Jun 26
**Theme: Writing CSV output and saving results**

**Minutes 0–30: Watch**
CS50P Lecture 6: **50:00 – end**

**Minutes 30–50: Coding task**
Create `csv_writer.py` — extend your Titanic analysis to write results:
```python
# Save analysis results back to CSV
import csv

# Load the same Titanic data
passengers = []
with open("titanic.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["Survived"] = int(row["Survived"])
        row["Pclass"] = int(row["Pclass"])
        row["Fare"] = float(row["Fare"]) if row["Fare"] else 0
        passengers.append(row)

# Add a "FareCategory" column based on fare amount
def categorize_fare(fare):
    if fare < 10:
        return "Budget"
    elif fare < 30:
        return "Standard"
    elif fare < 100:
        return "Premium"
    else:
        return "Luxury"

for p in passengers:
    p["FareCategory"] = categorize_fare(p["Fare"])

# Write enriched data to a new CSV
output_fields = ["PassengerId", "Name", "Survived", "Pclass", "Sex", "Age", "Fare", "FareCategory"]
with open("titanic_enriched.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=output_fields, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(passengers)

print("Saved titanic_enriched.csv")

# Summary by fare category
categories = ["Budget", "Standard", "Premium", "Luxury"]
print("\nSurvival by fare category:")
for cat in categories:
    group = [p for p in passengers if p["FareCategory"] == cat]
    if group:
        survived = sum(p["Survived"] for p in group)
        print(f"  {cat:<10}: {survived}/{len(group)} ({survived/len(group)*100:.0f}%)")
```

**Minutes 50–60: Commit**
```
git add csv_writer.py titanic_enriched.csv
git commit -m "Add CSV writer: enrich Titanic data with fare categories and write output"
git push
```

---

### Friday, Jun 27
**Theme: Week 7 review + build a data pipeline**

**Minutes 0–30: Watch**
FCC YouTube: **4:22:00 – 4:40:00**

**Minutes 30–50: Build a mini data pipeline**
Create `data_pipeline.py`:
```python
# Mini Data Pipeline
# Reads CSV → cleans data → analyzes → writes report
import csv
from datetime import datetime

def load_and_clean(filename):
    """Load CSV and remove rows with missing critical data."""
    clean = []
    skipped = 0
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row.get("Age") or not row.get("Fare"):
                skipped += 1
                continue
            row["Age"] = float(row["Age"])
            row["Fare"] = float(row["Fare"])
            row["Survived"] = int(row["Survived"])
            row["Pclass"] = int(row["Pclass"])
            clean.append(row)
    print(f"Loaded {len(clean)} rows, skipped {skipped} incomplete rows")
    return clean

def analyze(passengers):
    """Run analysis and return a results dict."""
    total = len(passengers)
    survived = sum(p["Survived"] for p in passengers)
    avg_age = sum(p["Age"] for p in passengers) / total
    avg_fare = sum(p["Fare"] for p in passengers) / total
    return {
        "total": total,
        "survived": survived,
        "survival_rate": survived / total,
        "avg_age": avg_age,
        "avg_fare": avg_fare,
    }

def write_report(results, filename):
    """Write analysis results to a text report."""
    with open(filename, "w") as f:
        f.write("=== TITANIC ANALYSIS REPORT ===\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write(f"Total passengers (with complete data): {results['total']}\n")
        f.write(f"Survivors: {results['survived']}\n")
        f.write(f"Survival rate: {results['survival_rate']*100:.1f}%\n")
        f.write(f"Average age: {results['avg_age']:.1f} years\n")
        f.write(f"Average fare: ${results['avg_fare']:.2f}\n")
    print(f"Report written to {filename}")

# Run the pipeline
passengers = load_and_clean("titanic.csv")
results = analyze(passengers)
write_report(results, "titanic_report.txt")
print("Pipeline complete.")
```

**Minutes 50–60: README + commit**
```
git add data_pipeline.py titanic_report.txt README.md
git commit -m "Complete Week 7: file I/O, CSV read/write, Titanic pipeline, report generation"
git push
```

---

## WEEK 8 — OOP Basics and NumPy

---

### Monday, Jun 30
**Theme: Classes and objects**

**Minutes 0–30: Watch**
FCC YouTube: **4:40:00 – 5:00:00**
Topics: classes, `__init__`, instance attributes

**Minutes 30–50: Coding task**
Create `classes_intro.py`:
```python
# Object-Oriented Programming fundamentals

class Student:
    """Represents a university student."""
    
    def __init__(self, name, major, gpa):
        """Initialize a Student. Called automatically when you create one."""
        self.name = name
        self.major = major
        self.gpa = gpa
        self.courses = []  # starts empty
    
    def enroll(self, course):
        """Add a course to the student's schedule."""
        self.courses.append(course)
        print(f"{self.name} enrolled in {course}")
    
    def drop(self, course):
        """Remove a course from the student's schedule."""
        if course in self.courses:
            self.courses.remove(course)
            print(f"{self.name} dropped {course}")
        else:
            print(f"{self.name} is not enrolled in {course}")
    
    def is_on_honor_roll(self):
        """Return True if GPA >= 3.5."""
        return self.gpa >= 3.5
    
    def __str__(self):
        """String representation — used by print()."""
        honor = " [Honor Roll]" if self.is_on_honor_roll() else ""
        return f"{self.name} | {self.major} | GPA: {self.gpa}{honor}"


# Create student objects
alice = Student("Alice Johnson", "Computer Science", 3.8)
bob = Student("Bob Kumar", "Mathematics", 3.2)

print(alice)
print(bob)

alice.enroll("CS101")
alice.enroll("AI201")
alice.enroll("MATH150")
bob.enroll("MATH201")
alice.drop("MATH150")

print(f"\nAlice's courses: {alice.courses}")
print(f"Alice on honor roll: {alice.is_on_honor_roll()}")
print(f"Bob on honor roll: {bob.is_on_honor_roll()}")
```

**Minutes 50–60: Commit**
```
git add classes_intro.py
git commit -m "Add OOP intro: Student class with attributes, methods, and __str__"
git push
```

---

### Tuesday, Jul 1
**Theme: NumPy — arrays and math**

**Minutes 0–30: Install and explore**
In your terminal:
```
pip install numpy
```
Then watch FCC YouTube: **5:00:00 – 5:20:00** (or search "NumPy tutorial beginners" on YouTube for a 20-min intro)

**Minutes 30–50: Coding task**
Create `numpy_intro.py`:
```python
# NumPy — fast numerical arrays (the foundation of AI/ML)
import numpy as np

# 1. Creating arrays
list_data = [1, 2, 3, 4, 5]
arr = np.array(list_data)
print("Array:", arr)
print("Type:", type(arr))
print("Data type:", arr.dtype)

# 2. Why numpy? Speed via vectorized operations
# Without numpy (slow):
scores_list = [85, 92, 78, 95, 88, 72, 91, 84]
# With numpy (fast, clean):
scores = np.array(scores_list)

print(f"\nScores: {scores}")
print(f"Mean:   {np.mean(scores):.2f}")
print(f"Median: {np.median(scores):.2f}")
print(f"Std Dev:{np.std(scores):.2f}")
print(f"Min:    {np.min(scores)}")
print(f"Max:    {np.max(scores)}")

# 3. Array math (applied to every element at once)
curved = scores + 5  # add 5 to every score
print(f"\nOriginal: {scores}")
print(f"Curved+5: {curved}")
print(f"Normalized (0-1): {(scores - scores.min()) / (scores.max() - scores.min())}")

# 4. Boolean indexing — filter arrays
passing = scores[scores >= 80]
print(f"\nPassing scores (>=80): {passing}")
print(f"Failing scores (<80):  {scores[scores < 80]}")

# 5. 2D arrays (matrices) — the data structure behind ML
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(f"\n2D array shape: {matrix.shape}")  # (3, 3)
print(f"Row 0: {matrix[0]}")
print(f"Column 1: {matrix[:, 1]}")
print(f"Element [1][2]: {matrix[1][2]}")
```

**Minutes 50–60: Commit**
```
git add numpy_intro.py
git commit -m "Add NumPy intro: arrays, vectorized math, boolean indexing, 2D arrays"
git push
```

---

### Wednesday, Jul 2
**Theme: NumPy continued — arange, reshape, random**

**Minutes 0–30: Watch**
CS50P Lecture 5: **0:00 – 25:00**
Topics: unit tests — important professional habit

**Minutes 30–50: Coding task**
Create `numpy_practice.py`:
```python
import numpy as np

# 1. Generating arrays
evens = np.arange(0, 21, 2)
print("Even numbers 0-20:", evens)

linspace = np.linspace(0, 1, 11)  # 11 evenly spaced from 0 to 1
print("0 to 1 in 10 steps:", linspace)

zeros = np.zeros(5)
ones = np.ones((3, 3))
print("Zeros:", zeros)
print("3x3 ones:\n", ones)

# 2. Random arrays — critical for ML
np.random.seed(42)  # seed for reproducibility (important concept!)
random_scores = np.random.randint(60, 101, size=50)  # 50 random scores 60-100
print(f"\n50 random scores:")
print(f"  Mean: {random_scores.mean():.1f}")
print(f"  Std:  {random_scores.std():.1f}")

# Grade distribution
print(f"  A (>=90): {np.sum(random_scores >= 90)}")
print(f"  B (80-89):{np.sum((random_scores >= 80) & (random_scores < 90))}")
print(f"  C (70-79):{np.sum((random_scores >= 70) & (random_scores < 80))}")
print(f"  Below 70: {np.sum(random_scores < 70)}")

# 3. Reshape — understanding tensor shapes (core ML concept)
flat = np.arange(12)         # [0, 1, 2, ..., 11]
matrix = flat.reshape(3, 4)  # 3 rows, 4 cols
print(f"\nFlat: {flat}")
print(f"Reshaped to 3x4:\n{matrix}")

# 4. Dot product (matrix multiplication) — the core operation of neural networks
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
dot = np.dot(a, b)  # 1*4 + 2*5 + 3*6 = 32
print(f"\nDot product of {a} and {b}: {dot}")
```

**Minutes 50–60: Commit**
```
git add numpy_practice.py
git commit -m "Add NumPy: arange, linspace, random arrays, reshape, dot product"
git push
```

---

### Thursday, Jul 3
**Theme: Phase 2 mini-project — NumPy data summary script**

**Minutes 0–30: Watch**
CS50P Lecture 5: **25:00 – end**

**Minutes 30–50: Build the mini-project**
Create `data_summary.py`:
```python
#!/usr/bin/env python3
"""
Data Summary Script
Generates statistical summary of numerical data from a CSV file.
Usage: python data_summary.py
"""
import numpy as np
import csv

def load_csv_column(filename, column_name):
    """Load a single numeric column from a CSV, skipping missing values."""
    values = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            val = row.get(column_name, "").strip()
            if val:
                try:
                    values.append(float(val))
                except ValueError:
                    pass
    return np.array(values)

def summarize(data, label):
    """Print a full statistical summary of a numpy array."""
    print(f"\n--- {label} ---")
    print(f"  Count:    {len(data)}")
    print(f"  Mean:     {np.mean(data):.2f}")
    print(f"  Median:   {np.median(data):.2f}")
    print(f"  Std Dev:  {np.std(data):.2f}")
    print(f"  Min:      {np.min(data):.2f}")
    print(f"  Max:      {np.max(data):.2f}")
    print(f"  25th pct: {np.percentile(data, 25):.2f}")
    print(f"  75th pct: {np.percentile(data, 75):.2f}")

# Load and analyze Titanic data
ages = load_csv_column("titanic.csv", "Age")
fares = load_csv_column("titanic.csv", "Fare")

print("=== TITANIC DATA SUMMARY ===")
summarize(ages, "Passenger Ages")
summarize(fares, "Ticket Fares")

# Correlation — do older passengers pay more?
# Match rows where both age and fare exist
pairs = []
with open("titanic.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["Age"] and row["Fare"]:
            try:
                pairs.append((float(row["Age"]), float(row["Fare"])))
            except:
                pass

ages_paired = np.array([p[0] for p in pairs])
fares_paired = np.array([p[1] for p in pairs])
correlation = np.corrcoef(ages_paired, fares_paired)[0][1]
print(f"\nCorrelation between age and fare: {correlation:.3f}")
print("(Close to 1.0 = strong positive, 0 = no relationship, -1.0 = inverse)")
```

**Minutes 50–60: README + commit**
```
git add data_summary.py README.md
git commit -m "Add data summary script: NumPy statistics on Titanic CSV, correlation"
git push
```

---

## PHASE 3 — AI-Adjacent Tools (Weeks 9–12)

---

## WEEK 9 — pandas

---

### Friday, Jul 4 (Independence Day — optional rest day)
**If you choose to work:**

**Minutes 0–30:**
Install pandas and Jupyter: `pip install pandas jupyter`
Watch the official 10-minute pandas intro: search YouTube for "pandas tutorial 10 minutes" (pandas official doc video)

**Minutes 30–50: Coding task**
Create `pandas_intro.py`:
```python
import pandas as pd

# Load the Titanic data — now with pandas instead of csv module
df = pd.read_csv("titanic.csv")

print("Shape:", df.shape)          # (rows, columns)
print("\nFirst 5 rows:")
print(df.head())
print("\nColumn info:")
print(df.info())
print("\nStatistical summary:")
print(df.describe())
print("\nMissing values:")
print(df.isnull().sum())
```

**Minutes 50–60: Commit**
```
git add pandas_intro.py
git commit -m "Add pandas intro: load CSV, head, info, describe, missing values"
git push
```

---

### Monday, Jul 7
**Theme: pandas filtering and selection**

**Minutes 0–30: Watch**
Search YouTube: "pandas dataframe filtering tutorial" — watch any 20-min video that covers `.loc`, boolean indexing, and `.value_counts()`

**Minutes 30–50: Coding task**
Create `pandas_filtering.py`:
```python
import pandas as pd

df = pd.read_csv("titanic.csv")

# 1. Select columns
print("Passenger names:")
print(df["Name"].head(5))

# 2. Multiple columns
print("\nName and Age:")
print(df[["Name", "Age", "Survived"]].head(8))

# 3. Filter rows — first class survivors
first_class_survivors = df[(df["Pclass"] == 1) & (df["Survived"] == 1)]
print(f"\nFirst class survivors: {len(first_class_survivors)}")
print(first_class_survivors[["Name", "Age", "Sex", "Fare"]].head())

# 4. Value counts
print("\nSurvivors by class:")
print(df.groupby("Pclass")["Survived"].sum())

print("\nGender breakdown:")
print(df["Sex"].value_counts())

print("\nSurvival rate by gender:")
print(df.groupby("Sex")["Survived"].mean().round(3))

# 5. Sort
youngest_survivors = df[df["Survived"] == 1].sort_values("Age").head(5)
print("\nFive youngest survivors:")
print(youngest_survivors[["Name", "Age", "Pclass", "Sex"]])
```

**Minutes 50–60: Commit**
```
git add pandas_filtering.py
git commit -m "Add pandas filtering: loc, boolean indexing, groupby, value_counts, sort"
git push
```

---

### Tuesday, Jul 8
**Theme: pandas — handling missing data**

**Minutes 0–30: Watch**
Search YouTube: "pandas handle missing data fillna dropna" — watch a 15–20 min tutorial

**Minutes 30–50: Coding task**
Create `pandas_cleaning.py`:
```python
import pandas as pd

df = pd.read_csv("titanic.csv")

print("=== BEFORE CLEANING ===")
print(f"Shape: {df.shape}")
print(f"Missing values:\n{df.isnull().sum()}\n")

# Strategy 1: Drop rows where Age is missing
df_dropped = df.dropna(subset=["Age"])
print(f"After dropna(Age): {df_dropped.shape[0]} rows")

# Strategy 2: Fill Age missing values with median age
median_age = df["Age"].median()
df_filled = df.copy()
df_filled["Age"] = df_filled["Age"].fillna(median_age)
print(f"After fillna(median={median_age}): still {df_filled.shape[0]} rows, {df_filled['Age'].isnull().sum()} missing")

# Strategy 3: Fill Embarked with mode (most common value)
mode_embarked = df["Embarked"].mode()[0]
df_filled["Embarked"] = df_filled["Embarked"].fillna(mode_embarked)

# Drop Cabin column (too many missing — 77% empty)
df_filled = df_filled.drop(columns=["Cabin"])

print("\n=== AFTER CLEANING ===")
print(f"Shape: {df_filled.shape}")
print(f"Missing values:\n{df_filled.isnull().sum()}")

# Save clean version
df_filled.to_csv("titanic_clean.csv", index=False)
print("\nSaved titanic_clean.csv")
```

**Minutes 50–60: Commit**
```
git add pandas_cleaning.py titanic_clean.csv
git commit -m "Add pandas data cleaning: dropna, fillna with median/mode, drop columns"
git push
```

---

### Wednesday, Jul 9
**Theme: pandas groupby and aggregation**

**Minutes 0–30: Watch**
Search YouTube: "pandas groupby tutorial" — 15–20 min

**Minutes 30–50: Coding task**
Create `pandas_groupby.py`:
```python
import pandas as pd

df = pd.read_csv("titanic_clean.csv")

# 1. Survival by passenger class
print("=== Survival Analysis ===\n")
class_analysis = df.groupby("Pclass").agg(
    total=("Survived", "count"),
    survivors=("Survived", "sum"),
    survival_rate=("Survived", "mean"),
    avg_age=("Age", "mean"),
    avg_fare=("Fare", "mean")
).round(2)
print("By passenger class:")
print(class_analysis)

# 2. Multi-level groupby: class AND gender
print("\nSurvival rate by class AND gender:")
cross = df.groupby(["Pclass", "Sex"])["Survived"].agg(["sum", "count", "mean"]).round(2)
cross.columns = ["survivors", "total", "rate"]
print(cross)

# 3. Add a new column: fare per person (Age group)
df["AgeGroup"] = pd.cut(df["Age"], bins=[0, 12, 18, 35, 60, 100],
                         labels=["Child", "Teen", "Young Adult", "Adult", "Senior"])

print("\nSurvival by age group:")
age_groups = df.groupby("AgeGroup")["Survived"].agg(["sum", "count", "mean"]).round(2)
age_groups.columns = ["survived", "total", "rate"]
print(age_groups)
```

**Minutes 50–60: Commit**
```
git add pandas_groupby.py
git commit -m "Add pandas groupby: multi-level aggregation, age bins, cross-tabulation"
git push
```

---

### Thursday, Jul 10
**Theme: Build the Project 2 Jupyter Notebook**

**Minutes 0–30: Launch Jupyter**
In your terminal:
```
pip install jupyter notebook
cd ~/Desktop/python-summer
jupyter notebook
```
A browser window opens. Click "New" → "Python 3 (ipykernel)" to create a new notebook.
Save it as `titanic_analysis.ipynb` in a `notebooks/` folder.

**Minutes 30–55: Build notebook**
In the notebook, create cells with these sections:
- Cell 1 (Markdown): `# Titanic Survival Analysis` + a 2-sentence description
- Cell 2: imports (`import pandas as pd`, `import numpy as np`)
- Cell 3: load data, `.head()`, `.info()`
- Cell 4: missing value analysis + cleaning (use your cleaning code)
- Cell 5: survival rate overall
- Cell 6: survival by class
- Cell 7: survival by gender
- Cell 8 (Markdown): `## Key Findings` + 3 bullet points describing what you found

**Minutes 55–60: Commit**
```
git add notebooks/titanic_analysis.ipynb
git commit -m "Add Titanic Jupyter notebook: EDA, cleaning, survival analysis, key findings"
git push
```

---

### Friday, Jul 11
**Theme: Week 9 review and polish**

**Minutes 0–30: Watch**
CS50P Lecture 8: **0:00 – 25:00** (OOP final review — connects to data classes)

**Minutes 30–50: Add a README to the notebooks folder**
Create `notebooks/README.md`:
```markdown
## Notebooks

### titanic_analysis.ipynb
Exploratory data analysis of the Titanic passenger dataset (891 records).

**Key findings:**
- Overall survival rate: 38.4%
- First-class passengers survived at 63% vs 24% for third class
- Women survived at 74% vs 19% for men
- Children under 12 had the highest survival rate

**Libraries used:** pandas, numpy
**Data source:** Kaggle / datasciencedojo/datasets
```
Also add to your main README:
```
## Week 9 — Completed
pandas: filtering, groupby, aggregation, data cleaning
Project 2 Jupyter Notebook: Titanic survival analysis
```
```
git add notebooks/README.md README.md
git commit -m "Complete Week 9: pandas EDA complete, Titanic notebook with findings"
git push
```

---

## WEEK 10 — matplotlib

---

### Monday, Jul 14
**Theme: matplotlib basics**

**Minutes 0–30: Watch**
Search YouTube: "matplotlib beginner tutorial Python" — watch any 20-min intro

**Minutes 30–50: Coding task**
Run this in your terminal first: `pip install matplotlib`
Create `matplotlib_intro.py`:
```python
import matplotlib.pyplot as plt
import numpy as np

# 1. Basic line chart
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 5, 4, 7, 8, 6, 9, 11, 10]

plt.figure(figsize=(8, 4))
plt.plot(x, y, color="steelblue", linewidth=2, marker="o", markersize=6)
plt.title("My First Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("charts/line_chart.png", dpi=150)
plt.show()
print("Saved line_chart.png")

# 2. Math function
x2 = np.linspace(-3, 3, 100)
y2 = x2 ** 2  # parabola

plt.figure(figsize=(8, 4))
plt.plot(x2, y2, color="coral", linewidth=2, label="y = x²")
plt.title("Quadratic Function")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("charts/parabola.png", dpi=150)
plt.show()
```
Create the `charts/` directory first: `mkdir charts`

**Minutes 50–60: Commit**
```
git add matplotlib_intro.py charts/
git commit -m "Add matplotlib intro: line charts, math functions, save to PNG"
git push
```

---

### Tuesday, Jul 15
**Theme: Bar charts and histograms**

**Minutes 0–30: Watch**
Continue any matplotlib tutorial: bar charts and histograms section (~20 min)

**Minutes 30–50: Coding task**
Create `charts_bar_hist.py`:
```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("titanic_clean.csv")

# 1. Bar chart: survival by class
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

survival_by_class = df.groupby("Pclass")["Survived"].mean() * 100
axes[0].bar(["1st Class", "2nd Class", "3rd Class"], survival_by_class,
            color=["#2196F3", "#FF9800", "#F44336"], alpha=0.85, edgecolor="white")
axes[0].set_title("Survival Rate by Passenger Class", fontsize=13)
axes[0].set_ylabel("Survival Rate (%)")
axes[0].set_ylim(0, 100)
for i, v in enumerate(survival_by_class):
    axes[0].text(i, v + 1, f"{v:.1f}%", ha="center", fontweight="bold")

# 2. Histogram: age distribution
axes[1].hist(df["Age"].dropna(), bins=20, color="steelblue", alpha=0.75, edgecolor="white")
axes[1].axvline(df["Age"].median(), color="red", linestyle="--", linewidth=2, label=f"Median: {df['Age'].median():.0f}")
axes[1].set_title("Age Distribution of Passengers", fontsize=13)
axes[1].set_xlabel("Age")
axes[1].set_ylabel("Number of Passengers")
axes[1].legend()

plt.tight_layout()
plt.savefig("charts/bar_and_histogram.png", dpi=150)
plt.show()
print("Saved bar_and_histogram.png")
```

**Minutes 50–60: Commit**
```
git add charts_bar_hist.py charts/bar_and_histogram.png
git commit -m "Add bar chart (survival by class) and histogram (age distribution)"
git push
```

---

### Wednesday, Jul 16
**Theme: Scatter plots**

**Minutes 0–30: Watch**
Search YouTube: "matplotlib scatter plot tutorial" (15 min)

**Minutes 30–50: Coding task**
Create `scatter_plots.py`:
```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("titanic_clean.csv")

# Scatter: Age vs Fare, colored by survival
fig, ax = plt.subplots(figsize=(10, 6))

survivors = df[df["Survived"] == 1]
non_survivors = df[df["Survived"] == 0]

ax.scatter(non_survivors["Age"], non_survivors["Fare"],
           alpha=0.4, color="#F44336", s=25, label="Did not survive")
ax.scatter(survivors["Age"], survivors["Fare"],
           alpha=0.6, color="#4CAF50", s=35, label="Survived")

ax.set_title("Age vs. Fare — Colored by Survival Outcome", fontsize=13)
ax.set_xlabel("Age")
ax.set_ylabel("Ticket Fare ($)")
ax.legend()
ax.set_ylim(0, 300)  # trim extreme outliers for visibility
ax.grid(True, alpha=0.3)

# Trend line (first glimpse at linear regression concept)
mask = df["Age"].notna() & df["Fare"].notna()
z = np.polyfit(df.loc[mask, "Age"], df.loc[mask, "Fare"], 1)
p = np.poly1d(z)
x_line = np.linspace(0, 80, 100)
ax.plot(x_line, p(x_line), "k--", alpha=0.5, linewidth=1.5, label="Trend")
ax.legend()

plt.tight_layout()
plt.savefig("charts/scatter_age_fare.png", dpi=150)
plt.show()
```

**Minutes 50–60: Commit**
```
git add scatter_plots.py charts/scatter_age_fare.png
git commit -m "Add scatter plot: age vs fare colored by survival, with trend line"
git push
```

---

### Thursday, Jul 17
**Theme: Add visualizations to the Jupyter notebook**

**Minutes 0–30: Watch**
CS50P Lecture 8: **25:00 – end** — final CS50P material

**Minutes 30–50: Extend your Titanic notebook**
Open `notebooks/titanic_analysis.ipynb` in Jupyter.
Add these cells at the end:
- Cell 9: Bar chart of survival by class (use your code from Tuesday)
- Cell 10: Histogram of age distribution
- Cell 11: Scatter plot (age vs fare by survival)
- Cell 12 (Markdown): `## Visual Conclusions` — write 2-3 sentences interpreting what the charts show.

Add to the top of the notebook:
```python
import matplotlib.pyplot as plt
%matplotlib inline
```

**Minutes 50–60: Commit**
```
git add notebooks/titanic_analysis.ipynb
git commit -m "Add 3 visualizations to Titanic notebook: bar, histogram, scatter"
git push
```

---

### Friday, Jul 18
**Theme: Multi-panel summary figure — portfolio-ready**

**Minutes 0–30:**
Review your charts from this week. Identify the 4 strongest visuals.

**Minutes 30–50: Build a summary dashboard figure**
Create `titanic_dashboard.py`:
```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("titanic_clean.csv")
plt.style.use("seaborn-v0_8-whitegrid")

fig, axes = plt.subplots(2, 2, figsize=(13, 9))
fig.suptitle("Titanic Passenger & Survival Analysis", fontsize=15, fontweight="bold", y=1.01)

# 1. Survival by class
ax1 = axes[0, 0]
rates = df.groupby("Pclass")["Survived"].mean() * 100
bars = ax1.bar(["1st", "2nd", "3rd"], rates, color=["#1565C0", "#1976D2", "#90CAF9"])
ax1.set_title("Survival Rate by Class")
ax1.set_ylabel("% Survived")
ax1.set_ylim(0, 80)
for bar, rate in zip(bars, rates):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, f"{rate:.0f}%", ha="center")

# 2. Survival by gender
ax2 = axes[0, 1]
gender_rates = df.groupby("Sex")["Survived"].mean() * 100
ax2.bar(["Female", "Male"], gender_rates, color=["#E91E63", "#2196F3"])
ax2.set_title("Survival Rate by Gender")
ax2.set_ylabel("% Survived")
ax2.set_ylim(0, 100)
for i, rate in enumerate(gender_rates):
    ax2.text(i, rate + 1, f"{rate:.0f}%", ha="center")

# 3. Age histogram by survival
ax3 = axes[1, 0]
ax3.hist(df[df["Survived"]==0]["Age"], bins=20, alpha=0.6, color="#F44336", label="Died")
ax3.hist(df[df["Survived"]==1]["Age"], bins=20, alpha=0.6, color="#4CAF50", label="Survived")
ax3.set_title("Age Distribution by Outcome")
ax3.set_xlabel("Age")
ax3.legend()

# 4. Fare box plot by class
ax4 = axes[1, 1]
class1 = df[df["Pclass"]==1]["Fare"]
class2 = df[df["Pclass"]==2]["Fare"]
class3 = df[df["Pclass"]==3]["Fare"]
ax4.boxplot([class1, class2, class3], labels=["1st", "2nd", "3rd"],
            patch_artist=True,
            boxprops=dict(facecolor="lightblue", color="navy"))
ax4.set_title("Fare Distribution by Class")
ax4.set_ylabel("Ticket Fare ($)")
ax4.set_ylim(0, 200)

plt.tight_layout()
plt.savefig("charts/titanic_dashboard.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved titanic_dashboard.png")
```

**Minutes 50–60: README + commit**
```
git add titanic_dashboard.py charts/titanic_dashboard.png
git commit -m "Complete Week 10: matplotlib charts complete, 4-panel dashboard figure"
git push
```

---

## WEEK 11 — scikit-learn and Machine Learning

---

### Monday, Jul 21
**Theme: What is ML? Train/test split**

**Minutes 0–30: Watch**
Search YouTube: "scikit-learn tutorial beginners" — watch the first 20–25 min (covers what ML is, train/test split)
Install: `pip install scikit-learn`

**Minutes 30–50: Coding task**
Create `ml_concepts.py`:
```python
# Machine Learning foundations
# Key concept: we train on some data, then TEST on data the model has NEVER seen

from sklearn.model_selection import train_test_split
import numpy as np

# Simulate a simple dataset: house sizes (sq ft) and prices ($1000s)
np.random.seed(42)
n = 100
house_sizes = np.random.randint(800, 3500, n)
# Price roughly: $150 per sq ft + random noise
prices = house_sizes * 150 + np.random.randint(-20000, 20000, n)

print(f"Dataset: {n} houses")
print(f"Size range: {house_sizes.min()} - {house_sizes.max()} sq ft")
print(f"Price range: ${prices.min():,} - ${prices.max():,}")

# Split: 80% for training, 20% for testing
X = house_sizes.reshape(-1, 1)  # scikit-learn needs 2D input
y = prices

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"\nTraining set: {len(X_train)} samples")
print(f"Testing set:  {len(X_test)} samples")
print("\nThe model will TRAIN on the training set.")
print("We will EVALUATE it on the test set — data it has never seen.")
print("This tells us how well the model generalizes to new data.")
```

**Minutes 50–60: Commit**
```
git add ml_concepts.py
git commit -m "Add ML concepts: train/test split, dataset creation, scikit-learn intro"
git push
```

---

### Tuesday, Jul 22
**Theme: Linear regression**

**Minutes 0–30: Watch**
Search YouTube: "scikit-learn linear regression tutorial" — 20 min

**Minutes 30–50: Coding task**
Create `linear_regression.py`:
```python
# Linear Regression — predicting a continuous value
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Create dataset
np.random.seed(42)
n = 100
sizes = np.random.randint(800, 3500, n).reshape(-1, 1)
prices = sizes.flatten() * 150 + np.random.randint(-25000, 25000, n)

# Split
X_train, X_test, y_train, y_test = train_test_split(sizes, prices, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)  # this is where "learning" happens

print(f"Learned relationship:")
print(f"  Price = {model.coef_[0]:.2f} × size + {model.intercept_:.2f}")
print(f"  (True relationship is approximately: price = 150 × size)")

# Evaluate on test set
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
print(f"\nTest set results:")
print(f"  R² score: {r2:.3f}  (1.0 = perfect, 0 = random)")
print(f"  RMSE: ${rmse:,.0f}  (average prediction error)")

# Make predictions on new data
new_sizes = np.array([[1000], [2000], [3000]])
predictions = model.predict(new_sizes)
for size, pred in zip(new_sizes.flatten(), predictions):
    print(f"\n  Predicted price for {size} sq ft: ${pred:,.0f}")

# Plot
plt.figure(figsize=(9, 5))
plt.scatter(X_test, y_test, alpha=0.6, color="steelblue", label="Actual")
plt.plot(X_test, y_pred, color="red", linewidth=2, label="Predicted")
plt.title("Linear Regression: House Size → Price")
plt.xlabel("Size (sq ft)")
plt.ylabel("Price ($)")
plt.legend()
plt.tight_layout()
plt.savefig("charts/linear_regression.png", dpi=150)
plt.show()
```

**Minutes 50–60: Commit**
```
git add linear_regression.py charts/linear_regression.png
git commit -m "Add linear regression: fit, predict, R² score, RMSE, visualization"
git push
```

---

### Wednesday, Jul 23
**Theme: Classification with the Iris dataset**

**Minutes 0–30: Watch**
Search YouTube: "scikit-learn classification tutorial iris" — 20 min

**Minutes 30–50: Coding task**
Create `classification_iris.py`:
```python
# Classification — predicting a category (not a number)
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the classic Iris dataset (built into scikit-learn)
iris = load_iris()
X = iris.data    # 4 features: sepal length, sepal width, petal length, petal width
y = iris.target  # 0=setosa, 1=versicolor, 2=virginica

print("Iris dataset:")
print(f"  Samples: {X.shape[0]}")
print(f"  Features: {X.shape[1]} ({', '.join(iris.feature_names)})")
print(f"  Classes: {iris.target_names}")

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train K-Nearest Neighbors classifier
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nKNN (k=3) Accuracy: {accuracy*100:.1f}%")
print(f"\nDetailed report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Predict on a new flower
new_flower = np.array([[5.1, 3.5, 1.4, 0.2]])  # known setosa
prediction = model.predict(new_flower)
probabilities = model.predict_proba(new_flower)[0]
print(f"\nNew flower prediction: {iris.target_names[prediction[0]]}")
print(f"Probabilities: { {iris.target_names[i]: f'{p:.0%}' for i, p in enumerate(probabilities)} }")
```

**Minutes 50–60: Commit**
```
git add classification_iris.py
git commit -m "Add KNN classification on Iris dataset: accuracy, classification report, prediction"
git push
```

---

### Thursday, Jul 24
**Theme: Confusion matrix and comparing models**

**Minutes 0–30: Watch**
Search YouTube: "confusion matrix scikit-learn explained" — 15 min

**Minutes 30–50: Coding task**
Create `model_comparison.py`:
```python
# Compare multiple classifiers on the same dataset
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "KNN (k=3)": KNeighborsClassifier(n_neighbors=3),
    "Decision Tree": DecisionTreeClassifier(max_depth=3, random_state=42),
    "Logistic Regression": LogisticRegression(max_iter=200, random_state=42),
}

print("=== MODEL COMPARISON ===\n")
best_model = None
best_score = 0

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"{name:<25} Accuracy: {acc*100:.1f}%")
    if acc > best_score:
        best_score = acc
        best_model = (name, model)

print(f"\nBest model: {best_model[0]} ({best_score*100:.1f}%)")

# Confusion matrix for best model
y_pred_best = best_model[1].predict(X_test)
cm = confusion_matrix(y_test, y_pred_best)
print(f"\nConfusion matrix ({best_model[0]}):")
print("Rows = Actual, Columns = Predicted")
print(f"Classes: {list(iris.target_names)}")
print(cm)
print("Diagonal = correct predictions, Off-diagonal = errors")
```

**Minutes 50–60: Commit**
```
git add model_comparison.py
git commit -m "Add model comparison: KNN vs Decision Tree vs Logistic Regression, confusion matrix"
git push
```

---

### Friday, Jul 25
**Theme: Week 11 review — end-to-end ML script**

**Minutes 0–30: Review**
Re-read `linear_regression.py`, `classification_iris.py`, and `model_comparison.py`. Draw on paper (or a text file): the steps of a supervised ML pipeline: Data → Split → Train → Predict → Evaluate.

**Minutes 30–50: Write the ML pipeline as a clean script**
Create `ml_pipeline_iris.py`:
```python
"""
Complete ML Pipeline — Iris Classification
This script demonstrates a full, reproducible machine learning workflow.
"""
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

def load_data():
    """Load the Iris dataset."""
    iris = load_iris()
    return iris.data, iris.target, iris.target_names

def preprocess(X_train, X_test):
    """Normalize features to zero mean and unit variance."""
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)  # IMPORTANT: use same scaler, don't fit again
    return X_train_scaled, X_test_scaled

def train_model(X_train, y_train):
    """Train a KNN classifier."""
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train, y_train)
    return model

def evaluate(model, X_test, y_test, class_names):
    """Evaluate and print results."""
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc*100:.1f}%")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=class_names))
    return acc

def main():
    print("=== Iris ML Pipeline ===\n")
    X, y, class_names = load_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    X_train, X_test = preprocess(X_train, X_test)
    model = train_model(X_train, y_train)
    evaluate(model, X_test, y_test, class_names)

main()
```

**Minutes 50–60: README + commit**
```
git add ml_pipeline_iris.py README.md
git commit -m "Complete Week 11: full ML pipeline with preprocessing, train, evaluate"
git push
```

---

## WEEK 12 — Project 2: Full ML Analysis Notebook

---

### Monday, Jul 28
**Theme: Titanic ML — feature engineering**

**Minutes 0–60: Build in Jupyter**
Create `notebooks/titanic_ml.ipynb`:

Cell 1 (Markdown): `# Titanic Survival Prediction — Machine Learning`

Cell 2:
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
%matplotlib inline

df = pd.read_csv("../titanic_clean.csv")
print(df.shape)
df.head()
```

Cell 3 — Feature Engineering:
```python
# Encode categorical variables for ML
df_ml = df.copy()

# Encode Sex: male=0, female=1
df_ml["Sex_encoded"] = (df_ml["Sex"] == "female").astype(int)

# Encode Embarked
embarked_map = {"S": 0, "C": 1, "Q": 2}
df_ml["Embarked_encoded"] = df_ml["Embarked"].map(embarked_map).fillna(0)

# Select features
features = ["Pclass", "Sex_encoded", "Age", "SibSp", "Parch", "Fare", "Embarked_encoded"]
X = df_ml[features]
y = df_ml["Survived"]

print("Features used:", features)
print(f"Dataset shape: {X.shape}")
X.head()
```

Cell 4 — Split:
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Train: {len(X_train)}, Test: {len(X_test)}")
```
Commit at end of session.
```
git add notebooks/titanic_ml.ipynb
git commit -m "Start Titanic ML notebook: feature engineering, encoding, split"
git push
```

---

### Tuesday, Jul 29
**Theme: Train and evaluate Titanic models**

**Minutes 0–60: Continue the notebook**
Add these cells:

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

models = {
    "Logistic Regression": LogisticRegression(max_iter=500),
    "Decision Tree": DecisionTreeClassifier(max_depth=4, random_state=42),
    "KNN": KNeighborsClassifier(n_neighbors=7),
}

results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    results[name] = acc
    print(f"{name}: {acc*100:.1f}%")

best = max(results, key=results.get)
print(f"\nBest model: {best} ({results[best]*100:.1f}%)")
```
Then add a bar chart of model accuracy scores.

**Minutes 55–60: Commit**
```
git add notebooks/titanic_ml.ipynb
git commit -m "Add 3 models to Titanic ML notebook: accuracy comparison and bar chart"
git push
```

---

### Wednesday, Jul 30
**Theme: Feature importance and interpretation**

**Minutes 0–60: Continue notebook**
Add these cells:

```python
# Feature importance from Decision Tree
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(max_depth=4, random_state=42)
dt.fit(X_train, y_train)

importance = pd.Series(dt.feature_importances_, index=features).sort_values(ascending=True)
importance.plot(kind="barh", figsize=(8, 5), color="steelblue")
plt.title("Feature Importance (Decision Tree)")
plt.xlabel("Importance Score")
plt.tight_layout()
plt.savefig("../charts/feature_importance.png", dpi=150)
plt.show()
```

Then add a Markdown cell:
```markdown
## Interpretation
The Decision Tree tells us that **Sex** is the most important predictor of survival, 
followed by **Pclass** (passenger class) and **Fare**. This aligns with the historical 
record — "women and children first" was applied more consistently for higher-class passengers.
```

**Minutes 55–60: Commit**
```
git add notebooks/titanic_ml.ipynb charts/feature_importance.png
git commit -m "Add feature importance chart and written interpretation to Titanic ML notebook"
git push
```

---

### Thursday, Jul 31
**Theme: Notebook conclusion and README**

**Minutes 0–50: Finalize the notebook**
Add a final Markdown summary cell:
```markdown
## Summary and Conclusions

### What we did
1. Loaded and cleaned the Titanic dataset (891 passengers, 7 features)
2. Engineered features: encoded Sex, Embarked; selected relevant columns
3. Trained 3 classifiers: Logistic Regression, Decision Tree, KNN
4. Evaluated on a held-out 20% test set

### Results
| Model | Accuracy |
|---|---|
| Logistic Regression | XX% |
| Decision Tree | XX% |
| KNN | XX% |

### Key Finding
Gender (Sex) is the strongest predictor of survival, with women having 74% survival 
vs 19% for men. Passenger class is the second strongest predictor.

### What I would do next with more time
- Try Random Forest (an ensemble of Decision Trees)
- Use cross-validation for more reliable accuracy estimates
- Add family size as a feature (SibSp + Parch + 1)
```

Update `notebooks/README.md` to include the ML notebook.

**Minutes 50–60: Commit**
```
git add notebooks/ README.md
git commit -m "Finalize Titanic ML notebook: summary, results table, next steps section"
git push
```

---

### Friday, Aug 1
**Theme: Week 12 polish — Project 2 GitHub presentation**

**Minutes 0–30:**
Create `projects/titanic-analysis/` folder structure:
```
projects/titanic-analysis/
├── data/              (copy titanic.csv and titanic_clean.csv here)
├── notebooks/         (copy your two notebooks here)
├── charts/            (copy your PNG charts here)
├── src/
│   └── pipeline.py    (copy titanic_analysis.py here, cleaned up)
├── requirements.txt
└── README.md
```
Create `requirements.txt`:
```
pandas>=2.0
numpy>=1.24
matplotlib>=3.7
scikit-learn>=1.3
jupyter>=1.0
```

**Minutes 30–50: Write the Project 2 README**
```markdown
# Titanic Survival Analysis & ML Prediction

End-to-end data analysis and machine learning project on the Titanic passenger dataset.

## Overview
Analyzed survival patterns across 891 passengers, then built and compared 3 ML classifiers.

## How to run
pip install -r requirements.txt
jupyter notebook notebooks/titanic_analysis.ipynb

## Results
- Best model: Decision Tree (XX% accuracy on held-out test set)
- Key predictor: Sex (gender) — largest single factor in survival
- Second predictor: Passenger class (1st class: 63% vs 3rd class: 24%)

## Files
- notebooks/titanic_analysis.ipynb — EDA with 4 visualizations
- notebooks/titanic_ml.ipynb — ML pipeline with 3 models
- charts/ — all generated figures

## Skills demonstrated
pandas, NumPy, matplotlib, scikit-learn, Jupyter, data cleaning, ML pipeline

## Data source
[Titanic dataset](https://www.kaggle.com/c/titanic) — public domain
```

**Minutes 50–60: Final commit**
```
git add projects/titanic-analysis/
git commit -m "Complete Project 2: Titanic analysis with EDA, 4 charts, 3 ML models, full README"
git push
```

---

## PHASE 4 — Capstone and Portfolio Polish (Weeks 13–14)

---

## WEEK 13 — Project 3: ML Prediction Tool (Capstone)

---

### Monday, Aug 4
**Theme: Design and scaffold the capstone**

**Minutes 0–20: Plan**
Create `projects/ml-predictor/` with this structure:
```
projects/ml-predictor/
├── data/
├── notebooks/
├── src/
│   ├── __init__.py
│   ├── load_data.py
│   ├── preprocess.py
│   ├── model.py
│   └── visualize.py
├── results/
├── .gitignore
├── requirements.txt
└── README.md
```

**Minutes 20–50: Build `src/load_data.py`**
```python
"""Load and inspect dataset."""
from sklearn.datasets import load_iris
import pandas as pd

def load():
    """Load Iris dataset as a DataFrame."""
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df["target"] = iris.target
    df["species"] = df["target"].map({0: "setosa", 1: "versicolor", 2: "virginica"})
    return df, iris.target_names

if __name__ == "__main__":
    df, classes = load()
    print(f"Loaded {len(df)} samples")
    print(df.head())
    print(df["species"].value_counts())
```

**Minutes 50–60: Commit**
```
git add projects/ml-predictor/
git commit -m "Scaffold capstone project: folder structure and load_data.py"
git push
```

---

### Tuesday, Aug 5
**Theme: Build preprocess.py and model.py**

**Minutes 0–60: Code**

`src/preprocess.py`:
```python
"""Feature preprocessing for ML pipeline."""
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

def split_and_scale(df, target_col="target", test_size=0.2, random_state=42):
    """Split dataset and scale features."""
    X = df.drop(columns=[target_col, "species"]).values
    y = df[target_col].values
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    return X_train, X_test, y_train, y_test, scaler
```

`src/model.py`:
```python
"""Train and evaluate ML models."""
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

MODELS = {
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "Decision Tree": DecisionTreeClassifier(max_depth=4, random_state=42),
    "Logistic Regression": LogisticRegression(max_iter=300, random_state=42),
}

def train_all(X_train, y_train):
    """Train all models and return fitted dict."""
    trained = {}
    for name, model in MODELS.items():
        model.fit(X_train, y_train)
        trained[name] = model
    return trained

def evaluate_all(trained_models, X_test, y_test, class_names):
    """Evaluate all models, print results, return scores."""
    scores = {}
    for name, model in trained_models.items():
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        scores[name] = acc
        print(f"\n{name}: {acc*100:.1f}%")
        print(classification_report(y_test, y_pred, target_names=class_names))
    return scores
```

**Minutes 55–60: Commit**
```
git add projects/ml-predictor/src/
git commit -m "Add preprocess.py (split+scale) and model.py (train+evaluate all models)"
git push
```

---

### Wednesday, Aug 6
**Theme: Build visualize.py and main runner**

**Minutes 0–50: Code**

`src/visualize.py`:
```python
"""Visualization functions for ML results."""
import matplotlib.pyplot as plt
import numpy as np

def plot_accuracy_comparison(scores, save_path="results/accuracy_comparison.png"):
    names = list(scores.keys())
    values = [v * 100 for v in scores.values()]
    
    plt.figure(figsize=(8, 5))
    bars = plt.bar(names, values, color=["#2196F3", "#4CAF50", "#FF9800"])
    plt.title("Model Accuracy Comparison — Iris Classification")
    plt.ylabel("Accuracy (%)")
    plt.ylim(80, 100)
    for bar, val in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                 f"{val:.1f}%", ha="center", fontweight="bold")
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"Saved: {save_path}")
```

Create `main.py` at project root:
```python
#!/usr/bin/env python3
"""
ML Predictor — Iris Classification Pipeline
Run: python main.py
"""
import sys
sys.path.insert(0, "src")

from load_data import load
from preprocess import split_and_scale
from model import train_all, evaluate_all
from visualize import plot_accuracy_comparison

def main():
    print("=== Iris ML Pipeline ===\n")
    df, class_names = load()
    X_train, X_test, y_train, y_test, _ = split_and_scale(df)
    trained = train_all(X_train, y_train)
    scores = evaluate_all(trained, X_test, y_test, class_names)
    plot_accuracy_comparison(scores)
    best = max(scores, key=scores.get)
    print(f"\nBest model: {best} ({scores[best]*100:.1f}%)")
    print("\nPipeline complete. Chart saved to results/")

if __name__ == "__main__":
    main()
```

**Minutes 50–60: Commit**
```
git add projects/ml-predictor/
git commit -m "Add visualize.py and main.py: full end-to-end pipeline runnable with python main.py"
git push
```

---

### Thursday, Aug 7
**Theme: Test, clean, and add docstrings**

**Minutes 0–50:**
Run `python main.py` from the `projects/ml-predictor/` directory. Fix any errors.
Then open each `.py` file and add or improve docstrings on every function.
Add inline comments explaining any line that isn't obvious.
Run it again. Take a screenshot of the terminal output and the saved chart.

**Minutes 50–60: Commit**
```
git add projects/ml-predictor/
git commit -m "Add docstrings, inline comments, verify full pipeline runs cleanly"
git push
```

---

### Friday, Aug 8
**Theme: Write Project 3 README**

**Minutes 0–50: Write the README**
```markdown
# ML Predictor — Iris Species Classifier

A modular machine learning pipeline that trains and compares three classifiers on the Iris dataset.

## How to run
cd projects/ml-predictor
pip install -r requirements.txt
python main.py

## Output
- Accuracy scores for 3 models printed to terminal
- Bar chart saved to results/accuracy_comparison.png

## Project structure
src/load_data.py    — dataset loading
src/preprocess.py   — train/test split and feature scaling
src/model.py        — train and evaluate all models
src/visualize.py    — generate output charts
main.py             — orchestrates the full pipeline

## Results
| Model | Accuracy |
|---|---|
| KNN (k=5) | 96.7% |
| Decision Tree (depth=4) | 96.7% |
| Logistic Regression | 100% |

## Skills demonstrated
Python OOP, modular code design, scikit-learn, StandardScaler, train/test split,
classification metrics, matplotlib, clean project structure, Git version control

## Why this matters for AI coursework
This pipeline mirrors the structure used in every ML course and research project:
load → preprocess → train → evaluate → visualize. Understanding each step
from scratch makes black-box frameworks like PyTorch easier to learn later.
```

**Minutes 50–60: Commit**
```
git add projects/ml-predictor/README.md
git commit -m "Complete Project 3 README: results, structure, skills, AI relevance"
git push
```

---

## WEEK 14 — Portfolio Polish and Launch

---

### Monday, Aug 11
**Theme: Polish all three project READMEs**

**Minutes 0–50:**
Open each of your three project READMEs. Check:
- Does it have a "How to run" section with exact commands?
- Does it have a results section with actual numbers?
- Is there a screenshot or sample output?
- Are skills listed clearly?
- Is there a "What I learned" or "Why this matters" section?

Fix any missing pieces. Add screenshot paths if you have them.

**Minutes 50–60: Commit everything**
```
git add .
git commit -m "Polish all three project READMEs: results, run instructions, skills"
git push
```

---

### Tuesday, Aug 12
**Theme: GitHub profile README**

**Minutes 0–50: Build your profile**
Go to github.com → click "+" → "New repository" → name it exactly your GitHub username (e.g., `jsmith`). Check "Add README file". Create it.

Clone it and write this in the README.md:
```markdown
# Hi, I'm [Your Name] 👋

I'm a student at Clemson University studying toward an AI minor.
This summer I've been building Python and ML skills from scratch, 
working toward my first AI coursework in the fall.

## Tech Stack
Python · NumPy · pandas · matplotlib · scikit-learn · Git · Jupyter

## Projects
| Project | Description | Key Skills |
|---|---|---|
| [Number Guessing Game](link) | CLI game with difficulty levels | Loops, functions, input validation |
| [Titanic Analysis](link) | EDA + ML on real passenger data | pandas, matplotlib, scikit-learn |
| [ML Predictor](link) | Modular iris classification pipeline | OOP, full ML pipeline, clean structure |

## Currently learning
- Python fundamentals (CS50P)
- Data analysis and visualization
- Intro to machine learning

📫 [your.email@g.clemson.edu] | [LinkedIn link]
```

**Minutes 50–60: Commit and push**
```
git add README.md
git commit -m "Create GitHub profile README with projects, tech stack, and contact"
git push
```

---

### Wednesday, Aug 13
**Theme: Resume bullet points**

**Minutes 0–50:**
Open a text editor (or Google Doc) and write your resume's "Projects" section:

```
PROJECTS

Number Guessing Game | Python                                     May 2025
Built a command-line game with three difficulty levels, loop-based game logic, and
input validation; tracked win/loss state across multiple rounds.

Titanic Survival Analysis | Python, pandas, matplotlib, scikit-learn  Jul 2025
Analyzed 891-record dataset; cleaned missing data, built 5 visualizations,
and compared 3 ML classifiers achieving up to 83% accuracy on held-out test data.

Iris ML Classification Pipeline | Python, scikit-learn, matplotlib      Aug 2025
Designed a modular ML pipeline (4 source files + main runner) training KNN,
Decision Tree, and Logistic Regression classifiers; best model reached 100% test accuracy.
```

Also draft your Skills section:
```
TECHNICAL SKILLS
Languages: Python
Libraries: NumPy, pandas, matplotlib, scikit-learn
Tools: Git, GitHub, Jupyter Notebook, VS Code
Concepts: Data analysis, supervised ML, feature engineering, data visualization
```

Save this as `resume_draft.md` in your repo's root.

**Minutes 50–60: Commit**
```
git add resume_draft.md
git commit -m "Add resume project bullets and skills section draft"
git push
```

---

### Thursday, Aug 14
**Theme: LinkedIn update**

**Minutes 0–50:**
Log into LinkedIn.

1. Under "About": write 3 sentences: who you are (student at Clemson, AI minor), what you've built this summer (Python/ML projects), what you're looking for (internship, research, or co-op in data/AI).

2. Under "Skills": add Python, NumPy, pandas, Data Analysis, Machine Learning, Git, Jupyter. (LinkedIn shows these to recruiters as searchable terms.)

3. Under "Projects": click "Add section" → "Projects". Add all three:
   - Include GitHub link for each
   - Copy the description from your resume bullets
   - Set date to the month completed

4. Under "Education": verify Clemson is listed. Add "Pursuing AI Minor" in the description field.

**Minutes 50–60: Final GitHub tidy**
```
git add .
git commit -m "Final tidy: update README, verify all projects linked and documented"
git push
```

---

### Friday, Aug 15 — FINAL DAY
**Theme: Review, celebrate, and plan next steps**

**Minutes 0–30: Full portfolio review**
Open each of your three GitHub repos. Check them as if you're a recruiter who just found them.
Ask: Is the README clear to someone who doesn't know Python? Does it show results? Would I know how to run it?
Fix any final issues.

**Minutes 30–50: Write a concepts log**
Create `WHAT_I_LEARNED.md` in your root repo:
```markdown
# What I Learned — Summer 2025

## Python fundamentals
- Variables, types, f-strings, input validation
- Control flow: if/elif/else, boolean logic
- Loops: for, while, break, continue, nested loops
- Functions: parameters, return values, default args, docstrings, scope

## Data structures
- Lists: indexing, slicing, comprehensions, sorting
- Dictionaries: CRUD, iteration, grouping data
- Sets: uniqueness, union, intersection

## File handling
- Text files: read, write, append
- CSV: csv.reader, csv.DictReader, csv.writer
- Building data pipelines

## AI-adjacent libraries
- NumPy: arrays, vectorized math, random, reshape, dot product
- pandas: DataFrame, filtering, groupby, missing data, merge
- matplotlib: line, bar, histogram, scatter, multi-panel figures
- scikit-learn: train_test_split, StandardScaler, KNN, Decision Tree, Logistic Regression, accuracy_score

## Professional skills
- Git: init, add, commit, push, meaningful commit messages
- GitHub: public repos, READMEs, project structure, profile README
- Jupyter Notebooks: EDA workflow, markdown + code cells, inline charts

## Projects built
1. Number Guessing Game
2. Titanic Survival Analysis (EDA + ML)
3. Iris ML Classification Pipeline (capstone)
```

**Minutes 50–60: Final commit**
```
git add WHAT_I_LEARNED.md
git commit -m "Add WHAT_I_LEARNED.md — summer 2025 complete"
git push
```

**You're done. You built 3 portfolio projects, 14 weeks of daily code, a GitHub ready to show a recruiter, and a real foundation for your AI minor. Day 1 of your first AI course will look very different than it would have without this summer.**

---

## Quick Reference: Daily Session Template

```
MINUTES 0–5:    Open yesterday's code. Can you explain it? Fix anything confusing.
MINUTES 5–30:   Watch the assigned content with your editor open. TYPE every example.
MINUTES 30–50:  Close the video. Build today's coding task from scratch.
MINUTES 50–60:  git add . → git commit -m "message" → git push
```

## Quick Reference: Commit Message Formula
```
Action verb + what you built + notable detail
✓ "Add grade checker using if/elif/else with 5 grade bands"
✓ "Fix infinite loop bug in guessing game"
✗ "update"
✗ "fixed stuff"
✗ "day 7"
```
