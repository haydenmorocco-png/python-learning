# Python & AI Daily Schedule — May 12 to August 15
> Every session = 60 minutes. Every day has exact tasks, timestamps, and commit messages.
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

Write a program that stores your name in a variable and prints three lines:
```
Hello, my name is [your name]
I am learning Python.
Today is Day 1.
```
Run it: open the VS Code terminal (Ctrl+` ) and type `python hello.py`. You should see all three lines. If you get an error, read it carefully — errors tell you exactly what went wrong.

**Minutes 50–60: GitHub setup**
1. Go to https://github.com and create a free account
2. Download Git from https://git-scm.com/downloads and install it
3. In your VS Code terminal, run these commands one by one:
```
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```
Add a comment at the bottom of `hello.py` that says "Day 1 complete. I set up Python, VS Code, and Git." Save the file. You'll push to GitHub tomorrow once the repo is created.

---

### Tuesday, May 13
**Theme: Variables and data types**

**Minutes 0–30: Watch**
FCC YouTube: **6:00 – 22:00**
Topics covered: variables, strings, integers, floats, booleans
While watching: every time they type something, pause and type it yourself in a new file called `variables.py`

**Minutes 30–50: Coding task**
In `variables.py`, write a program using your own real or made-up values. When run, it should print exactly 7 lines that look like this (with your own values):
```
Name: Alex Johnson
Age: 19
GPA: 3.7
Currently a student: True
Full name uppercase: ALEX JOHNSON
Name length: 4
Greeting: Hello, my name is Alex and I am 19 years old.
```
Requirements:
- Store first name, last name, age, GPA, and student status each in their own variable
- The uppercase line must use a string method, not be typed manually
- The greeting line must combine string and integer variables — you'll need to think about type conversion for that last one

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Getting started</summary>
Declare five variables at the top: first_name, last_name, age, gpa, is_student. Use quotes for strings, no quotes for numbers, and True/False (capital T/F) for booleans. Then write your print statements below.
</details>

<details>
<summary>Hint 2 — The uppercase line</summary>
Strings have built-in methods you call with a dot: `"hello".upper()` gives you `"HELLO"`. You can call this on a variable too. To combine two strings, use `+`.
</details>

<details>
<summary>Hint 3 — The greeting line crashes with a TypeError</summary>
You can't combine a string and an integer with `+` directly. Python needs them to be the same type. Look up `str()` — it converts a number into a string so you can join them.
</details>

</details>

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
In `strings.py`, write a program that asks the user for their name and a favorite number. When run with input "Alex" and 7, the output should look like this:
```
What is your name? Alex
What is your favorite number? 7

Hello, Alex!
Your name has 4 letters.
Your name in all caps: ALEX
Your favorite number doubled is 14.
Your favorite number squared is 49.
Your name contains the letter A or E.
```
Requirements:
- Use `input()` to collect both values
- Use f-strings for every print statement
- The last line should change depending on whether the name contains A or E — test it with "Lynn" to make sure it prints the other version
- Test with at least two different names

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Getting started</summary>
You need two variables. One stores a name (a string), one stores a number. Both come from `input()`. Try just getting those two lines working and printing them back before doing anything else.
</details>

<details>
<summary>Hint 2 — The math isn't working</summary>
`input()` always gives you a string, even if the user types a number. You can't do math on a string. Look up how to convert a string to an integer in Python.
</details>

<details>
<summary>Hint 3 — Counting the letters</summary>
Python has a built-in function that tells you the length of a string. You used it in the video. It works inside an f-string too: `f"something {function_here(variable)}"`.
</details>

<details>
<summary>Hint 4 — The last line isn't switching</summary>
You need an `if`/`else` here. The tricky part is checking for *either* A *or* E. Two things to think about: what keyword lets you check two conditions at once? And what happens if the user types "ALEX" in all caps — will your check still work?
</details>

</details>

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
Create `tip_calculator.py`. Build a tip calculator that asks the user for three things: the bill total, the tip percentage, and how many people are splitting the bill. When run with $50, 20%, and 3 people, the output should look like this:
```
=== Tip Calculator ===
Enter the bill total ($): 50
Enter tip percentage (e.g. 18 for 18%): 20
How many people are splitting the bill? 3

Bill total:    $50.00
Tip (20.0%):   $10.00
Total:         $60.00
Per person:    $20.00
```
Requirements:
- Bill and tip percentage should accept decimals (use `float`)
- Number of people should be a whole number (use `int`)
- All dollar amounts must be formatted to exactly 2 decimal places

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Getting started</summary>
Get all three inputs first and just print them back. Once that works, add the math one step at a time: tip amount, then total, then per-person share.
</details>

<details>
<summary>Hint 2 — The tip percentage math</summary>
If the user types 20, they mean 20%. To turn that into a decimal multiplier, divide by 100. Then multiply by the bill. So: `tip = bill * (tip_percent / 100)`.
</details>

<details>
<summary>Hint 3 — Formatting to 2 decimal places</summary>
Inside an f-string, you can format a number to 2 decimal places like this: `f"${amount:.2f}"`. The `.2f` means "fixed point, 2 decimal places."
</details>

</details>

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
Create `week1_review.py`. Without looking at any previous files, build a "personal info card" program from scratch. It should ask the user for their full name, birth year, hometown, and favorite subject, then print a formatted card. When run, it should look like this:
```
Enter your full name: alex johnson
Enter your birth year: 2006
Enter your hometown: greenville
Enter your favorite subject: computer science

=============================
       PERSONAL INFO CARD
=============================
Name:        Alex Johnson
Age:         19 years old
Hometown:    Greenville
Fav subject: computer science
Initials:    A.J.
=============================
```
Requirements:
- Name and hometown should be formatted with `.title()` so capitalization is correct regardless of how the user types it
- Age should be calculated from birth year, not typed in
- Initials should be extracted from the name automatically — figure out how to get the first letter of the first word and the first letter of the last word

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Getting started</summary>
Start with just the four inputs and printing them back. Then add the formatting one line at a time.
</details>

<details>
<summary>Hint 2 — Calculating age</summary>
You have the birth year as an integer. The current year is 2025. Subtraction gives you the age.
</details>

<details>
<summary>Hint 3 — Getting the initials</summary>
First, try printing `name.split()` — it shows you what that function does to a string. You'll see it turns the full name into a list of words. From there, index into position `[0]` for the first word and `[-1]` for the last word. Then use `[0]` again to get the first character of each word.
</details>

</details>

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
Create `grade_checker.py`. Write a program that asks for a score between 0 and 100, then prints the letter grade and a short feedback message. When run, it should look like this:
```
Enter your exam score (0-100): 83

Score: 83/100
Grade: B
Feedback: Good job!
```
Requirements:
- 90–100 → A, "Excellent work!"
- 80–89 → B, "Good job!"
- 70–79 → C, "Passing, but room to improve."
- 60–69 → D, "At risk. Consider getting a tutor."
- Below 60 → F, "Did not pass. Let's talk about next steps."
- Test with scores: 95, 83, 72, 65, 45 — each should give a different result

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Getting started</summary>
Get the input first and convert it to an integer. Then write a single `if` for the first grade band. Get that working before adding the other conditions.
</details>

<details>
<summary>Hint 2 — Structuring the conditions</summary>
You need `if / elif / elif / elif / else` — five branches total. Each condition only needs to check one boundary because Python checks top to bottom and stops at the first match. So if you've already eliminated ≥90, you don't need to check `score < 90` on the next line.
</details>

<details>
<summary>Hint 3 — Printing grade and message</summary>
Assign the letter grade and message to variables inside each branch, then print them once at the end outside the if/elif/else. This is cleaner than putting print statements inside each branch.
</details>

</details>

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
Create `eligibility_checker.py`. Write a program that asks a student four questions, then tells them whether they qualify for three different things. When run with GPA=3.8, 45 credits, full-time, no violations, it should print:
```
=== Eligibility Checker ===

Enter your GPA (0.0 - 4.0): 3.8
Enter completed credit hours: 45
Are you a full-time student? (yes/no): yes
Do you have any academic violations? (yes/no): no

--- Results ---
Merit Scholarship: Eligible
Honor Society:     Eligible
AI Club:           Eligible
```
Requirements:
- Merit scholarship: GPA ≥ 3.5 AND full-time AND no violations
- Honor society: GPA ≥ 3.7 AND at least 30 credits
- AI club: no violations (any GPA qualifies)
- Test with a case where someone qualifies for some but not all

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Converting yes/no input to a boolean</summary>
`input()` gives you a string. You need a True/False value. Try: `is_full_time = input("...").lower() == "yes"`. This compares the cleaned input to "yes" and gives you True or False automatically.
</details>

<details>
<summary>Hint 2 — Building the conditions</summary>
Use `and` to require multiple things to all be true. Use `not` to flip a boolean — so `not has_violations` is True when the student has no violations.
</details>

<details>
<summary>Hint 3 — The Eligible/Not eligible output</summary>
You can use a one-line conditional inside an f-string: `f"{'Eligible' if merit_eligible else 'Not eligible'}"`. Or just use a regular if/else — both work.
</details>

</details>

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
Create `bmi_calculator.py`. Write a program that asks whether to use metric or imperial units, collects the appropriate measurements, calculates BMI, and prints the result with a category. When run with metric input of 70 kg and 175 cm, it should print:
```
=== BMI Calculator ===

Use metric (kg/cm) or imperial (lb/in)? Enter 'm' or 'i': m
Weight in kg: 70
Height in cm: 175

Your BMI: 22.9
Category: Normal weight
(BMI is a rough estimate and not a medical diagnosis.)
```
Requirements:
- Metric formula: `weight / (height_in_meters ** 2)`
- Imperial formula: `(weight / (height_in_inches ** 2)) * 703`
- Categories: Under 18.5 = Underweight, 18.5–24.9 = Normal, 25–29.9 = Overweight, 30+ = Obese
- If the user types anything other than 'm' or 'i', print an error and skip the BMI output
- Round BMI to 1 decimal place

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Structuring the unit choice</summary>
Use `if unit == "m": ... elif unit == "i": ... else: ...`. Inside each branch, collect the inputs that are specific to that unit system.
</details>

<details>
<summary>Hint 2 — Converting height for metric</summary>
The formula needs height in meters, but the user enters centimeters. Divide by 100 to convert.
</details>

<details>
<summary>Hint 3 — Skipping the output on invalid input</summary>
Set `bmi = None` in the `else` branch. Then wrap the output section in `if bmi is not None:`. This is a clean pattern for "only proceed if we got valid data."
</details>

</details>

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

Complete **"Indoor Voice"**: a program that accepts one line of text and reprints it in all lowercase. Example:
```
Input:  HELLO THERE
Output: hello there
```

Then complete **"Playback Speed"**: a program that replaces every space in the input with `...`. Example:
```
Input:  This is CS50
Output: This...is...CS50
```

Submit both on edX if you have an account, or just run them locally.

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Indoor Voice</summary>
You need one line: get input, transform it, print it. Strings have a method that converts to lowercase — you used it on Tuesday.
</details>

<details>
<summary>Hint 2 — Playback Speed</summary>
Strings have a `.replace(old, new)` method. Call it on your input string with `" "` as the thing to replace and `"..."` as what to replace it with.
</details>

</details>

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
Create `decision_machine.py`. Build a programming language recommender that asks the user a few questions and gives a tailored recommendation. When run, it should look like this:
```
=== Programming Language Recommender ===

Answer a few questions and I'll recommend a language.

What's your main goal?
  1. AI/data science
  2. Web development
  3. Mobile apps
  4. General programming
Enter 1-4: 2

Do you have any coding experience? (yes/no): yes

--- Recommendation ---
Recommended: JavaScript + React
Reason: You already have a foundation — skip the basics and go straight to the industry standard framework.
```
Requirements:
- Goal 1 → always recommend Python
- Goal 2 → recommend JavaScript + React if experienced, HTML/CSS → JavaScript if not
- Goal 3 → recommend Swift or Kotlin
- Goal 4 → recommend Python with a math-related reason if they enjoy math, or Python as most beginner-friendly if they don't
- If the user enters something other than 1–4, print an error message
- Use boolean variables to store the yes/no answers before the decision logic

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Getting started</summary>
Collect all inputs first, then do all the logic after. Store your yes/no answers as booleans: `is_experienced = input("...").lower() == "yes"`.
</details>

<details>
<summary>Hint 2 — The nested recommendation for goal 2</summary>
You need an `if` inside an `elif`. The outer condition checks whether goal == 2. Inside that, a second `if` checks whether `is_experienced` is True.
</details>

<details>
<summary>Hint 3 — Converting the goal to an integer</summary>
`input()` gives you a string. You need to convert it to an integer with `int()` before you can compare it to numbers like 1 or 2. Do this conversion after collecting all inputs.
</details>

</details>

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
Create `loops_intro.py`. Write a program that demonstrates four things: counting, filtering, reversing, and generating a times table. When run with input 7, the output should look like this:
```
Counting to 10:
1 2 3 4 5 6 7 8 9 10

Even numbers 2-20:
2 4 6 8 10 12 14 16 18 20

Countdown:
10 9 8 7 6 5 4 3 2 1 Blast off!

Enter a number for its times table: 7

Times table for 7:
  7 x 1  = 7
  7 x 2  = 14
  ...
  7 x 12 = 84
```
Requirements:
- All three sequences (counting, evens, countdown) must be printed on a single line each using `end=" "`
- The even numbers must use the `step` parameter of `range()`, not an if statement
- The countdown must use a negative step
- The times table must go from 1 to 12
- Verify: 7 × 12 = 84

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Printing on one line</summary>
By default, `print()` adds a newline at the end. You can override this: `print(i, end=" ")` prints the number followed by a space instead of a new line. After the loop, call `print()` with no arguments to move to the next line.
</details>

<details>
<summary>Hint 2 — Even numbers with range()</summary>
`range()` takes up to three arguments: `range(start, stop, step)`. To count by twos starting at 2, use `range(2, 21, 2)`.
</details>

<details>
<summary>Hint 3 — Countdown</summary>
Use a negative step: `range(10, 0, -1)`. Notice the stop value is 0, not -1 — `range()` stops before reaching the stop value.
</details>

</details>

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
Create `while_loops.py`. Write two programs in the same file.

First, a counter that counts from 1 to 5 using a while loop:
```
Counting with while:
1
2
3
4
5
```

Then, a password gate that allows 3 attempts. When the wrong password is entered twice and the correct one third:
```
--- Password Gate ---
Enter password (attempt 1/3): wrong
Wrong password. 2 attempt(s) remaining.
Enter password (attempt 2/3): stillwrong
Wrong password. 1 attempt(s) remaining.
Enter password (attempt 3/3): clemson123
Access granted!
```
And when all three attempts fail:
```
Enter password (attempt 1/3): a
Wrong password. 2 attempt(s) remaining.
Enter password (attempt 2/3): b
Wrong password. 1 attempt(s) remaining.
Enter password (attempt 3/3): c
Too many failed attempts. Account locked.
```
Requirements:
- The counter must use a while loop with a variable that increments each iteration — forgetting to increment is the #1 cause of infinite loops
- The password gate must use `break` to exit early on a correct guess
- The "Account locked" message should only appear if the loop exhausted all attempts naturally (hint: look up `while/else` in Python)

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — The counter loop</summary>
You need a variable that starts at 1. The while condition checks if it's still ≤ 5. The last line inside the loop must increase the variable by 1: `count += 1`. Without that, the loop runs forever.
</details>

<details>
<summary>Hint 2 — Tracking attempts</summary>
Use a counter variable that starts at 0 and increments each loop iteration. Use it in the prompt string to show which attempt it is: `attempts + 1` (since you're incrementing after the prompt).
</details>

<details>
<summary>Hint 3 — The while/else trick</summary>
Python's `while` loop has an optional `else` clause that runs only if the loop ended normally (not via `break`). Structure: `while condition: ... else: print("locked")`. If `break` runs, the `else` is skipped entirely.
</details>

</details>

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
Create `nested_loops.py`. Build three pattern generators in the same file.

First, a 5×5 multiplication table grid (formatted so columns align):
```
Multiplication Table (1-5):

       1    2    3    4    5
   -------------------------
1 |    1    2    3    4    5
2 |    2    4    6    8   10
3 |    3    6    9   12   15
4 |    4    8   12   16   20
5 |    5   10   15   20   25
```

Then, a star triangle and number pyramid whose height the user controls. With input 5:
```
Star triangle:
*
**
***
****
*****

Number pyramid:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```
Requirements:
- The grid requires two nested loops — the outer loop handles rows, the inner handles columns
- The triangle and pyramid share the same `rows` variable from a single input
- Both patterns should work correctly for any number of rows the user enters

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — The grid header row</summary>
Print the column numbers first with a single loop, using `end=""` to keep them on one line. Then use `f"{i:4}"` to make each number take up exactly 4 characters so columns line up.
</details>

<details>
<summary>Hint 2 — The nested loop structure</summary>
The outer loop controls which row you're on (i). The inner loop controls which column (j). Inside the inner loop, print `i * j`. After the inner loop finishes (but still inside the outer), call `print()` to move to the next line.
</details>

<details>
<summary>Hint 3 — The star triangle</summary>
Row 1 has 1 star, row 2 has 2, row 3 has 3, etc. Your outer loop variable `i` goes from 1 to rows. The inner loop runs `i` times: `for j in range(i)`.
</details>

</details>

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
Create `fizzbuzz_plus.py`. This file has three parts.

First, the classic FizzBuzz from 1 to 30 — numbers divisible by 3 print "Fizz", by 5 print "Buzz", by both print "FizzBuzz", otherwise the number:
```
1
2
Fizz
4
Buzz
Fizz
7
...
FizzBuzz
```

Then, calculate and print the sum of every number from 1 to 1000 that is divisible by 3 or 5:
```
Sum of all multiples of 3 or 5 below 1001: 234168
```

Finally, count how many FizzBuzz numbers (divisible by both 3 and 5) exist between 1 and 100:
```
FizzBuzz numbers between 1 and 100: 6
```
Requirements:
- Use the modulo operator `%` for all divisibility checks
- The "divisible by both" case must be checked before the individual cases — think about why order matters here
- The sum and count can use a loop or a list comprehension

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — The modulo operator</summary>
`%` gives you the remainder of division. `10 % 3` is 1. `9 % 3` is 0. So `n % 3 == 0` is True when n is divisible by 3 with no remainder.
</details>

<details>
<summary>Hint 2 — Why order matters</summary>
If you check `% 3` first, a number like 15 will print "Fizz" and move on without ever checking the "divisible by both" case. Always check the most specific condition first — divisible by both 3 AND 5 — before the individual ones.
</details>

<details>
<summary>Hint 3 — The sum calculation</summary>
Start a variable `total = 0` before the loop. Inside the loop, add to it whenever the condition is met: `total += i`. Print `total` after the loop ends.
</details>

</details>

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
Re-read your `while_loops.py` and `fizzbuzz_plus.py`. You'll need: while loops, if/elif/else, the random module, and input validation.

**Minutes 5–50: Build Project 1**
Create `guessing_game.py` in a new folder `projects/guessing-game/`.

Build a number guessing game where the computer picks a secret number between 1 and 100 and the player tries to guess it. When run, a full session should look like this:
```
=================================
     NUMBER GUESSING GAME
=================================

Score: 0 wins, 0 losses

Choose difficulty — easy / medium / hard: medium

I've picked a number between 1 and 100.
You have 7 guesses. Good luck!

Guess 1/7: 50
Too high!
Guess 2/7: 25
Too low!
Guess 3/7: abc
Please enter a whole number.
Guess 3/7: 37
CORRECT! The number was 37.
You got it in 3 guess(es)!

Play again? (yes/no): no

Final score: 1 win(s), 0 loss(es). See you next time!
```
Requirements:
- Three difficulty levels: easy = 10 guesses, medium = 7, hard = 5
- If the player enters something that isn't a number, print an error and don't count it as a guess
- If the player enters a number outside 1–100, print an error and don't count it as a guess
- Track wins and losses across multiple rounds
- Put the game logic in a separate function called `play_game(difficulty)` that returns the number of guesses used on a win, or `None` on a loss
- Put the main loop (difficulty selection, play again prompt, score tracking) in a `main()` function

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Getting a random number</summary>
At the top of the file, write `import random`. Then use `random.randint(1, 100)` to get a random integer between 1 and 100 inclusive.
</details>

<details>
<summary>Hint 2 — Validating the input without crashing</summary>
Before converting the input to an integer, check whether it's all digits: `if not guess_str.isdigit()`. If it isn't, print the error and use `continue` to skip to the next loop iteration without counting the attempt.
</details>

<details>
<summary>Hint 3 — The while/else and break pattern</summary>
Structure your game loop as `while guesses_used < max_guesses:`. When the player guesses correctly, `return guesses_used` inside the loop (this exits the function entirely). If the loop ends naturally without a correct guess, the code after the loop runs — that's where you print the "out of guesses" message and `return None`.
</details>

<details>
<summary>Hint 4 — Connecting play_game() to main()</summary>
Call `result = play_game(difficulty)` inside your main loop. If `result is not None`, the player won — add to wins. If it's `None`, add to losses. Then ask if they want to play again.
</details>

</details>

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
Create `functions_intro.py`. Write five functions that demonstrate different ways functions work, then call each one. The output should be:
```
Hello! Welcome to Python.
Hello, Alex! Welcome to Python.
15 + 27 = 42
100°C = 212.0°F
98.6°F = 37.0°C
-10°C (14.0°F) — freezing
5°C (41.0°F) — cold
20°C (68.0°F) — comfortable
35°C (95.0°F) — hot
```
Requirements:
- A function with no parameters that just prints a greeting
- A function that takes a name and prints a personalized greeting
- A function that takes two numbers, adds them, and returns the result
- Two conversion functions: `celsius_to_fahrenheit` and `fahrenheit_to_celsius` — each takes one number and returns the converted value
- A `describe_temp` function that calls `celsius_to_fahrenheit` internally and returns a formatted string with the temperature, the converted value, and a word description (freezing/cold/comfortable/hot)
- Call `describe_temp` in a loop for the temperatures -10, 5, 20, 35

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Defining a function</summary>
`def function_name(parameter):` starts a function. Everything indented below it is part of the function. `return value` sends a value back to whoever called the function.
</details>

<details>
<summary>Hint 2 — Using a return value</summary>
When a function returns something, capture it: `result = add(15, 27)`. Then you can use `result` in a print statement.
</details>

<details>
<summary>Hint 3 — A function calling another function</summary>
Inside `describe_temp`, call `celsius_to_fahrenheit(celsius)` just like you would anywhere else. Store the result in a local variable and use it to build your return string.
</details>

</details>

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
Create `functions_advanced.py`. This file demonstrates three advanced function patterns. The output should look like:
```
Medium coffee, 1 shot(s), with milk
Large coffee, 1 shot(s), with milk
Small coffee, 2 shot(s), black
Medium coffee, 3 shot(s), black

Test scores: [88, 72, 95, 61, 83, 79, 91, 68]
Lowest:  61
Highest: 95
Average: 79.6

$1000 at 7% for 10 years: $1967.15
```
Requirements:
- A `make_coffee` function with three parameters — size, milk, and shots — all with default values so it can be called with zero, one, or all arguments
- A `get_stats` function that takes a list of numbers and returns three values at once: minimum, maximum, and average (look up how Python handles multiple return values)
- A `compound_interest` function with a full docstring explaining its arguments and return value
- Call `make_coffee` four different ways: with no arguments, overriding just size, overriding all three, and using keyword arguments

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Default parameter values</summary>
In the function definition, set defaults with `=`: `def make_coffee(size="medium", milk=True, shots=1):`. When you call the function without arguments, it uses these defaults.
</details>

<details>
<summary>Hint 2 — Returning multiple values</summary>
`return minimum, maximum, average` returns a tuple of three values. To capture all three: `low, high, avg = get_stats(scores)`. Python unpacks the tuple automatically.
</details>

<details>
<summary>Hint 3 — Writing a docstring</summary>
A docstring goes immediately after the `def` line, inside triple quotes. It should explain what the function does, what each parameter means, and what it returns. This is what appears when you call `help(compound_interest)`.
</details>

</details>

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
Open your `tip_calculator.py` from Week 1. Rewrite it from scratch as `tip_calculator_v2.py`, this time splitting every piece of logic into its own function. The output should be identical to the original, but the code should have at least four functions:

- One that handles getting valid bill input (with a loop that retries on bad input)
- One that calculates the tip amount
- One that calculates each person's share
- One that prints the formatted summary
- A `main()` function that calls all of the above

When run with the same inputs as before ($50, 20%, 3 people), the output should be:
```
=== Tip Calculator v2 ===

Enter the bill total ($): 50
Tip percentage (e.g. 18): 20
Number of people splitting: 3

==============================
       BILL SUMMARY
==============================
  Bill total:     $50.00
  Tip (20.0%):    $10.00
  Total:          $60.00
  People:         3
  Per person:     $20.00
==============================
```
The key difference from v1: if the user enters letters instead of a number for the bill, it should print "Please enter a valid number." and ask again instead of crashing.

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Validating input without crashing</summary>
Wrap the conversion in a `try/except ValueError` block. If `float(input(...))` fails because the user typed letters, the `except` block catches the error and you can print a message and loop again.
</details>

<details>
<summary>Hint 2 — The validation loop pattern</summary>
`while True:` with a `return` inside when input is valid is a clean pattern. The loop keeps asking until the user gives you something usable, then the function returns the value.
</details>

<details>
<summary>Hint 3 — Keeping functions focused</summary>
Each function should do one thing. `calculate_tip(bill, percentage)` just does the math and returns the result. It doesn't print anything. `print_summary(...)` handles all the printing. `main()` connects everything.
</details>

</details>

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
Complete **"Deep Thought"** from CS50P PS1. The program asks one question and checks if the answer is 42:
```
Input:  42    → Output: Yes!
Input:  41    → Output: No.
```

Then complete **"Home Federal Savings Bank"** — greet differently based on the first word of the input:
```
Input: Hello, there    → Output: $0
Input: How are you?    → Output: $20
Input: What's up?      → Output: $100
```
- Starts with "hello" (case-insensitive) → $0
- Starts with any other "h" word → $20
- Anything else → $100

Both programs must use a `main()` function.

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Deep Thought</summary>
Get input, convert to integer, compare to 42. That's it. Wrap in `def main():` and call `main()` at the bottom.
</details>

<details>
<summary>Hint 2 — Home Federal: case sensitivity</summary>
The user might type "Hello", "HELLO", or "hello". Use `.strip().lower()` on the input before checking it so capitalization doesn't matter.
</details>

<details>
<summary>Hint 3 — Home Federal: checking the start</summary>
Strings have a `.startswith("h")` method that returns True if the string begins with that character. Check `.startswith("hello")` first (most specific), then `.startswith("h")`, then the else catches everything else.
</details>

</details>

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
Create `unit_converter.py`. Build a menu-driven unit converter that runs in a loop until the user quits. When run, it should look like this:
```
=== Unit Converter ===
1. Miles → Kilometers
2. Kilograms → Pounds
3. Liters → Gallons
4. Quit

Enter choice (1-4): 1
Enter miles: 26.2
26.2 miles = 42.16 km

=== Unit Converter ===
1. Miles → Kilometers
...

Enter choice (1-4): 4
Goodbye!
```
Requirements:
- Each conversion must be its own function that takes a number and returns the converted value (look up the conversion factors)
- A separate `show_menu()` function prints the menu
- A `main()` function runs the loop
- Invalid menu choices print an error instead of crashing
- The menu re-displays after each conversion

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Conversion factors</summary>
1 mile = 1.60934 km. 1 kg = 2.20462 lbs. 1 liter = 0.264172 gallons. Each conversion function takes one number, multiplies by the factor, and returns the result.
</details>

<details>
<summary>Hint 2 — The menu loop</summary>
Use `while True:` with `break` when the user chooses 4. Call `show_menu()` at the top of the loop so it re-appears after each conversion.
</details>

<details>
<summary>Hint 3 — Handling invalid choices</summary>
Add an `else` at the end of your if/elif chain: `else: print("Invalid choice. Please enter 1, 2, 3, or 4.")`. The loop continues automatically, showing the menu again.
</details>

</details>

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
Create `lists_intro.py`. Using a list of five fruits and a list of ten numbers, write a program that demonstrates indexing, slicing, list methods, and membership testing. The output should include:
```
All fruits: ['apple', 'banana', 'cherry', 'date', 'elderberry']
First fruit: apple
Last fruit: elderberry
First three: ['apple', 'banana', 'cherry']
Last two: ['date', 'elderberry']
Reversed: ['elderberry', 'date', 'cherry', 'banana', 'apple']

After append: ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
After insert at index 2: ['apple', 'banana', 'blueberry', 'cherry', 'date', 'elderberry', 'fig']
After remove 'date': ['apple', 'banana', 'blueberry', 'cherry', 'elderberry', 'fig']
Popped: fig, Remaining: ['apple', 'banana', 'blueberry', 'cherry', 'elderberry']
Sorted: ['apple', 'banana', 'blueberry', 'cherry', 'elderberry']

Numbers: [34, 17, 89, 42, 56, 23, 71, 8, 95, 61]
Length: 10  Sum: 496  Min: 8  Max: 95  Average: 49.6

Enter a number to search for: 42
42 is in the list at index 3
```
Requirements:
- Use negative indexing for "Last fruit"
- Use slice notation `[::-1]` for "Reversed"
- Use `.append()`, `.insert()`, `.remove()`, `.pop()`, and `.sort()`
- The search at the end uses `input()` and checks membership with `in`

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Negative indexing</summary>
`fruits[-1]` gives you the last element. `fruits[-2]` gives the second-to-last. Python counts backward from the end.
</details>

<details>
<summary>Hint 2 — Slice notation</summary>
`fruits[start:stop]` gives a sub-list. Leave `start` empty to begin from the beginning: `fruits[:3]`. Leave `stop` empty to go to the end: `fruits[-2:]`. Use `[::-1]` to reverse: it means "step backwards through the whole list."
</details>

<details>
<summary>Hint 3 — Finding the index of an item</summary>
Once you've confirmed the item is `in` the list, use `numbers.index(target)` to find its position.
</details>

</details>

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
Create `list_comprehensions.py`. Write a program that demonstrates five uses of list comprehensions. The output should look like:
```
Squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Even squares: [4, 16, 36, 64, 100]
Uppercase: ['HELLO', 'WORLD', 'PYTHON', 'IS', 'GREAT']
Long words (>4 chars): ['hello', 'world', 'python', 'great']

Raw temps: [72, -1, 68, 75, -5, 80, 71, 999, 69, 74]
Valid temps: [72, 68, 75, 80, 71, 69, 74]
Average valid temp: 72.7°F

Fahrenheit: [32, 68, 86, 104, 212]
Celsius:    [0.0, 20.0, 30.0, 40.0, 100.0]
```
Requirements:
- All five results must be built using list comprehensions, not regular loops
- The temperature filter must reject values below 0 and above 120
- The Fahrenheit-to-Celsius conversion formula is `(f - 32) * 5/9`
- Round each Celsius value to 1 decimal place inside the comprehension

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Basic list comprehension syntax</summary>
`[expression for item in iterable]` — the expression is what you want each element to be, built from `item`. Example: `[x**2 for x in range(1, 11)]` makes a list of squares.
</details>

<details>
<summary>Hint 2 — Adding a filter</summary>
Add an `if` at the end: `[x**2 for x in range(1, 11) if x % 2 == 0]` — only even numbers get squared. The `if` condition filters which items are included.
</details>

<details>
<summary>Hint 3 — Multiple conditions in the filter</summary>
You can use `and` in the `if` part: `[t for t in raw_temps if t >= 0 and t <= 120]`.
</details>

</details>

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
Create `student_scores.py`. Given a list of student dictionaries (each with a name and score), produce a ranked leaderboard with grades, class statistics, and an above-average list. The output should look like:
```
=== CLASS RANKINGS ===
  1. Charlie     95  (A)
  2. Grace        91  (A)
  3. Alice        88  (B)
  4. Eve          83  (B)
  5. Frank        79  (C)
  6. Bob          72  (C)
  7. Henry        68  (D/F)
  8. Diana        61  (D/F)

Class average: 79.6
Highest: 95  |  Lowest: 61
Above average: Charlie, Grace, Alice, Eve
```
Requirements:
- Start with a hardcoded list of 8 student dicts — each with "name" and "score" keys
- Sort the list by score descending before printing
- Grades: ≥90=A, ≥80=B, ≥70=C, below 70=D/F
- The "Above average" line only includes students whose score is at or above the class average
- Rankings start at 1 (look up `enumerate`)

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Sorting a list of dicts</summary>
`sorted()` takes a `key` argument — a function that tells it what to sort by. To sort by score: `sorted(students, key=lambda s: s["score"], reverse=True)`. The `lambda` creates a small anonymous function on the spot.
</details>

<details>
<summary>Hint 2 — Printing with rank numbers</summary>
`enumerate(ranked, start=1)` gives you pairs of (rank, student) as you loop. Unpack them: `for i, student in enumerate(ranked, start=1):`.
</details>

<details>
<summary>Hint 3 — The above-average list</summary>
First calculate the average from all scores. Then use a list comprehension to filter: `[s["name"] for s in students if s["score"] >= avg]`. Use `", ".join(...)` to print them comma-separated.
</details>

</details>

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
Create `word_counter_v1.py`. Given a paragraph of text (hardcoded), count the frequency of each word and display the top 10 with a visual bar chart made of block characters. The output should look like:
```
Total words: 34
Unique words: 19

Top 10 most frequent words:
python          5  █████
is              3  ███
data            2  ██
a               2  ██
...
```
Requirements:
- Convert all words to lowercase before counting
- Strip punctuation from each word (`.` `,` `!` `?` `;` `:`) before counting
- Skip empty strings
- Sort the results by frequency descending before printing
- The bar is made by repeating the `"█"` character once per occurrence

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Splitting and cleaning</summary>
`text.lower().split()` gives you a list of lowercase words, but they may still have punctuation attached. Call `.strip(".,!?;:")` on each word to remove leading/trailing punctuation characters.
</details>

<details>
<summary>Hint 2 — Counting with a dictionary</summary>
Start with `frequency = {}`. For each cleaned word: if it's already a key, add 1 to its value. If not, set it to 1. This is the manual pattern — later you'll see `dict.get()` as a shortcut.
</details>

<details>
<summary>Hint 3 — Sorting dictionary items</summary>
`frequency.items()` gives you key-value pairs. Wrap it in `sorted(..., key=lambda x: x[1], reverse=True)` to sort by count descending. Then slice `[:10]` for the top 10.
</details>

</details>

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
Create `lotto_simulator.py`. Simulate buying 10 lottery tickets and see how you do against the winning numbers. The output should look like:
```
Winning numbers: [4, 12, 23, 31, 38, 47]

Ticket 1:  [3, 7, 12, 19, 38, 45]  →  2 match(es) [12, 38]  $0
Ticket 2:  [4, 12, 23, 31, 38, 47]  →  6 match(es) [4, 12, 23, 31, 38, 47]  $1000000
...

Total spent: $20
Total won:   $1000000
Net result:  $999980
```
Requirements:
- A `generate_ticket()` function that returns a sorted list of 6 unique random numbers between 1 and 49
- A `check_ticket(ticket, winning_numbers)` function that returns the count of matches and the list of matching numbers
- A `prize(matches)` function that returns: 6 matches=$1,000,000 / 5=$1,000 / 4=$100 / 3=$10 / 0-2=$0
- Each ticket costs $2
- Print a running total of spent and won at the end

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Generating unique numbers</summary>
Use a while loop: keep adding random numbers to a list until it has 6 items, but only add a number if it's not already in the list. Then sort the list before returning it.
</details>

<details>
<summary>Hint 2 — Finding matches</summary>
A list comprehension works well here: `[num for num in ticket if num in winning_numbers]`. This gives you the list of matching numbers. Use `len()` to count them.
</details>

<details>
<summary>Hint 3 — The prize function</summary>
A dictionary is clean for this: `prizes = {6: 1000000, 5: 1000, 4: 100, 3: 10, 2: 0, 1: 0, 0: 0}`. Then `return prizes[matches]`.
</details>

</details>

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
Create `dicts_intro.py`. Build a program that creates a student profile dictionary, demonstrates CRUD operations, iterates it, and then works with a dictionary of course enrollment lists. The output should include:
```
Name: Jordan Smith
GPA: 3.6
Keys: ['name', 'age', 'major', 'gpa', 'is_student']
Values: ['Jordan Smith', 20, 'Computer Science', 3.6, True]
Minor: Undeclared

Updated person: {'name': 'Jordan Smith', ..., 'minor': 'Artificial Intelligence', 'gpa': 3.7}

All info:
  name: Jordan Smith
  age: 20
  ...

AI301 students: ['Bob', 'Charlie', 'Diana', 'Frank']
Number of AI301 students: 4
Alice's courses: ['CS101', 'MATH201']
```
Requirements:
- Use `.get("minor", "Undeclared")` for the safe access line — do not use `person["minor"]` directly
- Add a "minor" key and update the GPA after creating the dict
- Iterate using `.items()` to print all key-value pairs
- The `alice_courses` list must be built with a list comprehension, not a regular loop

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Creating a dictionary</summary>
`person = {"name": "Jordan", "age": 20}` creates a dict. Access a value: `person["name"]`. Add or update a key: `person["minor"] = "AI"`.
</details>

<details>
<summary>Hint 2 — Safe access with .get()</summary>
`person.get("minor", "Undeclared")` returns the value if the key exists, or "Undeclared" if it doesn't. This won't crash if the key is missing, unlike `person["minor"]`.
</details>

<details>
<summary>Hint 3 — Finding Alice's courses with a comprehension</summary>
Loop through `courses.items()` — each item is a (course_name, student_list) pair. Include the course_name if "Alice" is in the student_list: `[course for course, students in courses.items() if "Alice" in students]`.
</details>

</details>

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
Create `word_frequency.py`. Upgrade your word counter from last week into a proper project-quality version with clean functions and a formatted report. When run on a provided AI-themed text passage, the output should look like:
```
Total words: 52
Unique words: 31

Top 15 words:
-----------------------------------
  artificial         4  (7.7%)
  intelligence       4  (7.7%)
  learning           3  (5.8%)
  neural             3  (5.8%)
  ...

Results saved to word_freq_output.txt
```
Requirements:
- A `clean_word(word)` function that lowercases and strips punctuation
- A `count_words(text)` function that returns a frequency dictionary — skip words of 1 character or less
- A `top_n_words(frequency, n)` function that returns the top n items sorted by count
- A `print_report(frequency)` function that prints the formatted output including percentages
- Save the full results (all words, sorted by frequency) to `word_freq_output.txt`

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Using dict.get() for counting</summary>
`frequency[word] = frequency.get(word, 0) + 1` is a clean one-liner for counting. If the word isn't in the dict yet, `.get()` returns 0, so you start at 1. If it is, you add 1 to the existing count.
</details>

<details>
<summary>Hint 2 — Calculating percentage</summary>
Total words is the sum of all values: `sum(frequency.values())`. Each word's percentage is `count / total * 100`.
</details>

<details>
<summary>Hint 3 — Writing to a file</summary>
`with open("word_freq_output.txt", "w") as f:` opens a file for writing. Inside the block, use `f.write(f"{word}: {count}\n")` to write each line. The `\n` adds a newline after each entry.
</details>

</details>

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
Create `sets_practice.py`. Demonstrate four things sets are useful for: automatic deduplication, set operations between two groups, removing duplicates from a list, and fast membership testing. The output should look like:
```
Colors set: {'red', 'green', 'blue'}
Number of unique colors: 3

Students in both courses: {'Bob', 'Diana', 'Eve'}
Students in either course: {'Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace'}
Python only: {'Alice', 'Charlie'}

Raw tags: ['python', 'AI', 'python', 'machine learning', 'AI', 'python', 'data']
Unique tags: ['AI', 'data', 'machine learning', 'python']

  alice_j: VALID
  hacker_x: INVALID
  bob_k: VALID
  unknown_user: INVALID
```
Requirements:
- Create a set with duplicate entries and show that they disappear automatically
- Define two student sets and compute intersection (`&`), union (`|`), and difference (`-`)
- Convert a list with duplicates to a set and back to a sorted list to deduplicate it
- Use a set (not a list) for the valid username check — this is faster for large data

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Creating a set</summary>
Use curly braces: `colors = {"red", "blue", "green", "red", "blue"}`. The duplicates are silently ignored. Note: an empty set must use `set()` not `{}` (which creates an empty dict).
</details>

<details>
<summary>Hint 2 — Set operators</summary>
`&` = intersection (in both), `|` = union (in either), `-` = difference (in first but not second). These work directly between two set variables.
</details>

<details>
<summary>Hint 3 — Deduplicating a list</summary>
`list(set(raw_tags))` converts to a set (removes duplicates) then back to a list. Wrap it in `sorted()` to get alphabetical order since sets have no guaranteed order.
</details>

</details>

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
Create `contacts.py`. Build a simple contacts manager that uses a dictionary as a database. It should support adding, finding, listing, and deleting contacts from a menu loop. When run, it should look like:
```
Added contact: Alice Johnson
Added contact: Bob Kumar
Added contact: Charlie Diaz

=== Contacts ===
1. Add contact
2. Find contact
3. List all
4. Delete contact
5. Quit
Choice: 3

--- All Contacts (3) ---
  Alice Johnson        555-0101
  Bob Kumar            555-0102
  Charlie Diaz         555-0103

Choice: 2
Search name: alice johnson

  Name:  Alice Johnson
  Phone: 555-0101
  Email: alice@example.com
```
Requirements:
- The dictionary key should be the name in lowercase so searches aren't case-sensitive
- `add_contact`, `find_contact`, `list_all`, and `delete_contact` should each be their own function
- Pre-load three contacts before showing the menu
- `list_all` should sort contacts alphabetically
- Finding or deleting a name that doesn't exist should print a helpful message instead of crashing

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Storing the data</summary>
Use `contacts[name.lower()] = {"phone": phone, "email": email, "name": name}`. The lowercase key makes lookups case-insensitive. Keep the original-cased name as a value so it displays correctly.
</details>

<details>
<summary>Hint 2 — Safe deletion</summary>
Check before deleting: `if name.lower() in contacts: del contacts[name.lower()]`. If the key isn't there, print "not found" instead.
</details>

<details>
<summary>Hint 3 — Sorting the contacts list</summary>
`for key in sorted(contacts):` iterates over keys in alphabetical order. Since keys are lowercase names, this gives you alphabetical output automatically.
</details>

</details>

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
Create `inventory.py`. Given a hardcoded inventory dictionary (items with price, quantity, and category), produce an analysis report. The output should look like:
```
Total inventory value: $312.45
Low stock items: ['cheese']
Categories: {'dairy', 'produce', 'bakery'}
Most expensive: cheese at $4.99

By category:
  bakery: bread
  dairy: cheese, milk, yogurt
  produce: apple, banana
```
Requirements:
- Calculate total value as the sum of `price * quantity` for all items
- Low stock = any item with fewer than 20 units
- Extract unique categories using a set comprehension
- Find the most expensive item using `max()` with a key function
- Group items by category into a dict of lists, then print them sorted

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Total value with a generator</summary>
`sum(item["price"] * item["quantity"] for item in inventory.values())` — this is a generator expression (like a list comprehension but without the brackets). It's efficient for summing on the fly.
</details>

<details>
<summary>Hint 2 — Set comprehension for categories</summary>
`{item["category"] for item in inventory.values()}` — uses curly braces instead of square brackets to produce a set directly.
</details>

<details>
<summary>Hint 3 — Grouping with setdefault()</summary>
`by_category.setdefault(cat, []).append(name)` is a clean pattern: if the key doesn't exist yet, it creates it with an empty list, then appends. Avoids needing to check `if cat in by_category` first.
</details>

</details>

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
Create `file_io.py`. Write a program that demonstrates all the basic file operations: writing, reading the whole file, reading line by line, appending, and searching. The program should create a file called `notes.txt`, manipulate it, and print results:
```
Writing to file...
File written.

Reading entire file:
Day 1: Variables and data types
Day 2: Strings and f-strings
...

Reading line by line:
  Line 1: Day 1: Variables and data types
  Line 2: Day 2: Strings and f-strings
  ...

File now has 6 lines.

Lines containing 'Functions':
  Day 4: Functions
```
Requirements:
- Write 5 topic lines to `notes.txt` (write mode — creates or overwrites)
- Read and print the entire file as one string
- Read and print line by line with line numbers using `enumerate`
- Append a 6th line using append mode (does not overwrite)
- Read all lines into a list and search for a term, printing matching lines

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — The with statement</summary>
`with open("notes.txt", "w") as f:` opens the file and automatically closes it when the block ends. The mode string matters: "w" = write (overwrite), "r" = read, "a" = append.
</details>

<details>
<summary>Hint 2 — Writing multiple lines</summary>
Each `f.write("text\n")` writes one line. The `\n` is the newline character — without it, everything runs together on one line.
</details>

<details>
<summary>Hint 3 — readlines() vs read()</summary>
`f.read()` gives you the whole file as one string. `f.readlines()` gives you a list of lines (each ending with `\n`). Use `.strip()` when printing to remove the trailing newline.
</details>

</details>

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
First, create `create_sample_csv.py`. This script, when run, creates a `students.csv` file with 8 student records (name, major, GPA, year, scholarship). You provide the data — make up realistic values.

Then create `csv_analysis.py` that reads the CSV and produces this output:
```
Loaded 8 students

Average GPA: 3.45

Top students (GPA >= 3.7):
  Charlie Diaz         3.9  Physics
  Alice Johnson        3.8  Computer Science
  Grace Kim            3.7  AI

Students per major:
  AI: 1
  Computer Science: 2
  ...

Scholarship holders: Alice Johnson, Charlie Diaz, Diana Lee, Grace Kim
```
Requirements:
- Use `csv.DictReader` to load the CSV — this gives you each row as a dictionary
- Convert GPA to float after loading (it comes in as a string)
- The scholarship holders line uses `", ".join(...)`

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Writing a CSV</summary>
`import csv`, open the file with `newline=""` to avoid extra blank lines on Windows, then `csv.writer(f).writerows(data)` where data is a list of lists (first list = headers).
</details>

<details>
<summary>Hint 2 — Reading with DictReader</summary>
`csv.DictReader(f)` treats the first row as column headers and gives you each subsequent row as a dict. You can then do `row["GPA"]` instead of `row[2]`.
</details>

<details>
<summary>Hint 3 — Counting by major</summary>
Use a dictionary: `majors = {}`. Loop through students: `majors[s["Major"]] = majors.get(s["Major"], 0) + 1`. This is the same counting pattern from the word frequency exercise.
</details>

</details>

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
Download the Titanic dataset by creating and running `download_titanic.py`:
```python
import urllib.request
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
urllib.request.urlretrieve(url, "titanic.csv")
print("Downloaded titanic.csv")
```
Then watch CS50P Lecture 6: **28:00 – 50:00**

**Minutes 30–50: Coding task**
Create `titanic_analysis.py`. Load the Titanic CSV and produce a survival analysis report. The output should look like:
```
Total passengers: 891

Survival rate: 38.4%
Class 1: 136/216 survived (63.0%)
Class 2: 87/184 survived (47.3%)
Class 3: 119/491 survived (24.2%)

Average age: 29.7

Male:   109/577 survived (18.9%)
Female: 233/314 survived (74.2%)
```
Requirements:
- Write a `load_titanic(filename)` function that handles the CSV loading and type conversion
- Convert Age, Fare, Survived, and Pclass to appropriate numeric types — use `None` for missing Age values
- Skip missing ages when calculating the average (don't divide by the total passenger count)
- Use list comprehensions for filtering groups

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Handling missing values</summary>
Some rows have an empty string for Age. Check before converting: `float(row["Age"]) if row["Age"] else None`. Then when calculating the average, filter out Nones: `[p["Age"] for p in passengers if p["Age"] is not None]`.
</details>

<details>
<summary>Hint 2 — Survival rate calculation</summary>
Filter to survivors: `survivors = [p for p in passengers if p["Survived"] == 1]`. The rate is `len(survivors) / len(passengers) * 100`.
</details>

<details>
<summary>Hint 3 — Survival by class in a loop</summary>
Loop `for pclass in [1, 2, 3]:`. Inside, filter twice: once for everyone in that class, once for survivors in that class. Then calculate the rate from those two filtered lists.
</details>

</details>

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
Create `csv_writer.py`. Load the Titanic data, add a new "FareCategory" column to each row based on fare amount, write the enriched data to a new CSV, then print a survival breakdown by fare category:
```
Saved titanic_enriched.csv

Survival by fare category:
  Budget    : 85/328 (26%)
  Standard  : 76/229 (33%)
  Premium   : 80/169 (47%)
  Luxury    : 31/55 (56%)
```
Requirements:
- Fare categories: Budget = under $10, Standard = $10–$29, Premium = $30–$99, Luxury = $100+
- Write a `categorize_fare(fare)` function
- Use `csv.DictWriter` with `extrasaction="ignore"` to write only selected columns to the output file
- Include a header row in the output

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Adding a column to each row</summary>
After loading, loop through passengers and add the new key: `p["FareCategory"] = categorize_fare(p["Fare"])`. This modifies each dict in place.
</details>

<details>
<summary>Hint 2 — DictWriter setup</summary>
`fieldnames = ["PassengerId", "Name", "Survived", ...]` — list only the columns you want in the output. Then `csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")` — `extrasaction="ignore"` tells it to skip any keys in the dict that aren't in fieldnames.
</details>

<details>
<summary>Hint 3 — Writing the header</summary>
Call `writer.writeheader()` before `writer.writerows(passengers)` — this writes the column names as the first row.
</details>

</details>

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
Create `data_pipeline.py`. Build a three-stage pipeline that loads and cleans the Titanic CSV, runs an analysis, and writes a text report to disk. When run, the terminal should show:
```
Loaded 714 rows, skipped 177 incomplete rows
Report written to titanic_report.txt
Pipeline complete.
```
And `titanic_report.txt` should contain:
```
=== TITANIC ANALYSIS REPORT ===
Generated: 2025-06-27 14:32

Total passengers (with complete data): 714
Survivors: 290
Survival rate: 40.6%
Average age: 29.4 years
Average fare: $34.69
```
Requirements:
- A `load_and_clean(filename)` function that skips rows missing Age or Fare, converts types, and prints how many were skipped
- An `analyze(passengers)` function that returns a results dictionary
- A `write_report(results, filename)` function that writes the formatted text file
- Use `datetime.now()` from the `datetime` module for the timestamp

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Skipping incomplete rows</summary>
Inside your loading loop: `if not row.get("Age") or not row.get("Fare"): skipped += 1; continue`. The `continue` skips to the next iteration without appending the incomplete row.
</details>

<details>
<summary>Hint 2 — The results dictionary</summary>
`analyze()` should calculate everything and return `{"total": ..., "survived": ..., "survival_rate": ..., "avg_age": ..., "avg_fare": ...}`. Then `write_report()` just formats and writes those values.
</details>

<details>
<summary>Hint 3 — Formatting the timestamp</summary>
`from datetime import datetime` then `datetime.now().strftime('%Y-%m-%d %H:%M')` gives you a formatted date-time string.
</details>

</details>

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
Create `classes_intro.py`. Define a `Student` class and demonstrate it. When run, the output should look like:
```
Alice Johnson | Computer Science | GPA: 3.8 [Honor Roll]
Bob Kumar | Mathematics | GPA: 3.2

Alice Johnson enrolled in CS101
Alice Johnson enrolled in AI201
Alice Johnson enrolled in MATH150
Bob Kumar enrolled in MATH201
Alice Johnson dropped MATH150

Alice's courses: ['CS101', 'AI201']
Alice on honor roll: True
Bob on honor roll: False
```
Requirements:
- The class needs: `name`, `major`, `gpa` as constructor parameters, and `courses` as an empty list that each instance starts with
- Methods: `enroll(course)` adds a course and prints a message, `drop(course)` removes a course (or prints an error if not enrolled), `is_on_honor_roll()` returns True if GPA ≥ 3.5
- A `__str__` method that produces the single-line summary shown in the first two lines of output (with `[Honor Roll]` appended only when GPA ≥ 3.5)
- Create two Student objects and call methods on them to produce the full output above

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — The __init__ method</summary>
`def __init__(self, name, major, gpa):` runs automatically when you create a Student. Inside it, `self.name = name` stores the value as an instance attribute. Add `self.courses = []` here too — don't put it as a parameter.
</details>

<details>
<summary>Hint 2 — The __str__ method</summary>
`def __str__(self):` must return a string. When you call `print(alice)`, Python calls this method automatically. Build the string using f-strings and conditional logic for the honor roll tag.
</details>

<details>
<summary>Hint 3 — The drop method</summary>
Check if the course is in `self.courses` before removing it. If it's there, use `.remove()`. If not, print an error message. This prevents a crash if the student tries to drop a course they're not in.
</details>

</details>

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
In your terminal: `pip install numpy`
Then watch FCC YouTube: **5:00:00 – 5:20:00** (or search "NumPy tutorial beginners" on YouTube for a 20-min intro)

**Minutes 30–50: Coding task**
Create `numpy_intro.py`. Demonstrate why NumPy is useful compared to plain Python lists. The output should include:
```
Array: [1 2 3 4 5]
Type: <class 'numpy.ndarray'>
Data type: int64

Scores: [85 92 78 95 88 72 91 84]
Mean:   85.62
Median: 86.50
Std Dev:7.16
Min:    72
Max:    95

Original: [85 92 78 95 88 72 91 84]
Curved+5: [90 97 83 100 93 77 96 89]
Normalized (0-1): [0.565 1.    0.261 1.    0.696 0.    0.826 0.522]

Passing scores (>=80): [85 92 95 88 91 84]
Failing scores (<80):  [78 72]

2D array shape: (3, 3)
Row 0: [1 2 3]
Column 1: [2 5 8]
Element [1][2]: 6
```
Requirements:
- Convert a Python list to a NumPy array and print its type and dtype
- Create a scores array and compute mean, median, std, min, max using NumPy functions
- Demonstrate vectorized math: add 5 to every score in one line (no loop needed)
- Demonstrate normalization: `(scores - scores.min()) / (scores.max() - scores.min())`
- Filter the array using boolean indexing: `scores[scores >= 80]`
- Create a 3×3 matrix and access a row, a column (using `:`), and a single element

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Creating a NumPy array</summary>
`import numpy as np` then `arr = np.array([1, 2, 3, 4, 5])`. This looks like a list but has superpowers: `arr + 5` adds 5 to every element at once. With a regular list, `list + 5` would crash.
</details>

<details>
<summary>Hint 2 — Boolean indexing</summary>
`scores >= 80` produces an array of True/False values. When you use that as an index — `scores[scores >= 80]` — NumPy returns only the elements where True appears. No loop needed.
</details>

<details>
<summary>Hint 3 — Accessing a column in a 2D array</summary>
`matrix[1]` gives you row 1. For a column, use a colon for the row: `matrix[:, 1]` means "all rows, column 1." The colon means "everything."
</details>

</details>

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
Create `numpy_practice.py`. Demonstrate four more NumPy capabilities. The output should include:
```
Even numbers 0-20: [ 0  2  4  6  8 10 12 14 16 18 20]
0 to 1 in 10 steps: [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1. ]
Zeros: [0. 0. 0. 0. 0.]
3x3 ones:
 [[1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]]

50 random scores:
  Mean: 80.3
  Std:  11.2
  A (>=90): 11
  B (80-89): 14
  C (70-79): 13
  Below 70: 12

Flat: [ 0  1  2  3  4  5  6  7  8  9 10 11]
Reshaped to 3x4:
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]

Dot product of [1 2 3] and [4 5 6]: 32
```
Requirements:
- Use `np.arange()` for evens, `np.linspace()` for the 0-to-1 sequence, `np.zeros()` and `np.ones()`
- Set `np.random.seed(42)` before generating random numbers (this makes results reproducible — important in ML)
- Use NumPy's compound boolean condition syntax for the B grade range: `(scores >= 80) & (scores < 90)` (note `&` not `and`)
- Use `.reshape()` to turn a flat array into a matrix
- Use `np.dot()` for the dot product and verify the result: 1×4 + 2×5 + 3×6 = 32

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — arange vs linspace</summary>
`np.arange(0, 21, 2)` counts by a step (like range). `np.linspace(0, 1, 11)` gives you exactly 11 evenly-spaced values between 0 and 1 inclusive.
</details>

<details>
<summary>Hint 2 — Why & instead of and</summary>
`and` works on single True/False values. When you have an array of booleans, you need element-wise operators: `&` for AND, `|` for OR. Parentheses are required: `(arr >= 80) & (arr < 90)`.
</details>

<details>
<summary>Hint 3 — reshape()</summary>
`flat.reshape(3, 4)` rearranges the 12 elements into 3 rows and 4 columns. The total number of elements must stay the same — you can't reshape a 12-element array into (3, 5).
</details>

</details>

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
Create `data_summary.py`. Write a script that loads one or more numeric columns from a CSV file and prints a full statistical summary for each, plus a correlation between two columns. When run on the Titanic CSV, the output should look like:
```
=== TITANIC DATA SUMMARY ===

--- Passenger Ages ---
  Count:    714
  Mean:     29.70
  Median:   28.00
  Std Dev:  14.53
  Min:      0.42
  Max:      80.00
  25th pct: 20.12
  75th pct: 38.00

--- Ticket Fares ---
  Count:    891
  ...

Correlation between age and fare: 0.096
(Close to 1.0 = strong positive, 0 = no relationship, -1.0 = inverse)
```
Requirements:
- A `load_csv_column(filename, column_name)` function that returns a NumPy array of floats, skipping missing/invalid values
- A `summarize(data, label)` function that uses NumPy functions for all statistics including `np.percentile()`
- Calculate the correlation using `np.corrcoef()` — you'll need to pair up rows where both Age and Fare are present

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Loading a column safely</summary>
In your CSV loop, try converting each value to float inside a try/except. If it fails (empty string, "N/A", etc.), just skip that row. Append successful values to a list, then `np.array(values)` at the end.
</details>

<details>
<summary>Hint 2 — np.percentile()</summary>
`np.percentile(data, 25)` gives the 25th percentile. `np.percentile(data, 75)` gives the 75th. These are the quartiles commonly shown in data summaries.
</details>

<details>
<summary>Hint 3 — np.corrcoef()</summary>
`np.corrcoef(array1, array2)` returns a 2×2 matrix. The correlation value you want is at position `[0][1]` (or equivalently `[1][0]`). Make sure both arrays have the same length — only include rows where both values are present.
</details>

</details>

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
Create `pandas_intro.py`. Load the Titanic CSV using pandas and print four things: the shape of the dataset, the first 5 rows, a column info summary, statistical descriptions of numeric columns, and a count of missing values per column. The output should include lines like:
```
Shape: (891, 12)

First 5 rows:
   PassengerId  Survived  Pclass  ...

Column info:
<class 'pandas.core.frame.DataFrame'>
...

Statistical summary:
       PassengerId    Survived      Pclass  ...

Missing values:
PassengerId      0
Age            177
Cabin          687
...
```
Requirements:
- `df.shape`, `df.head()`, `df.info()`, `df.describe()`, `df.isnull().sum()` — one per section
- This is an exploration exercise. Spend time looking at what each output tells you about the data.

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Loading with pandas</summary>
`import pandas as pd` then `df = pd.read_csv("titanic.csv")`. That's it — pandas handles all the CSV parsing automatically, including headers.
</details>

<details>
<summary>Hint 2 — What each method tells you</summary>
`.shape` = (rows, columns). `.head()` = first 5 rows. `.info()` = column names, types, and non-null counts. `.describe()` = statistics for numeric columns. `.isnull().sum()` = count of missing values per column.
</details>

</details>

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
Create `pandas_filtering.py`. Use the Titanic DataFrame to produce five outputs demonstrating different selection and filtering techniques:
```
Passenger names:
0                              Braund, Mr. Owen Harris
...

First class survivors: 136
   Name                     Age    Sex   Fare
   ...

Survivors by class:
Pclass
1    136
2     87
3    119

Gender breakdown:
male      577
female    314

Survival rate by gender:
Sex
female    0.742
male      0.189

Five youngest survivors:
   Name                   Age  Pclass  Sex
   ...
```
Requirements:
- Select a single column with `df["column"]`
- Filter with multiple conditions using `&` and `==`
- Use `.groupby()` with `.sum()`, `.value_counts()`, and `.mean()`
- Use `.sort_values()` to find the youngest survivors

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Multi-condition filtering</summary>
`df[(df["Pclass"] == 1) & (df["Survived"] == 1)]` — each condition in parentheses, joined with `&`. Using `and` instead of `&` will give you an error with pandas.
</details>

<details>
<summary>Hint 2 — groupby + aggregation</summary>
`df.groupby("Pclass")["Survived"].sum()` groups by class and sums the Survived column. `.mean()` instead of `.sum()` gives the survival rate (since Survived is 0 or 1, the mean equals the proportion).
</details>

<details>
<summary>Hint 3 — Sorting and slicing</summary>
`df.sort_values("Age")` sorts by age ascending. Chain `.head(5)` to get the first 5. Then select specific columns with `[["Name", "Age", "Pclass", "Sex"]]`.
</details>

</details>

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
Create `pandas_cleaning.py`. Show the before and after of three data cleaning strategies on the Titanic dataset. The output should include:
```
=== BEFORE CLEANING ===
Shape: (891, 12)
Missing values:
Age       177
Cabin     687
Embarked    2
...

After dropna(Age): 714 rows
After fillna(median=28.0): still 891 rows, 0 missing

=== AFTER CLEANING ===
Shape: (891, 11)
Missing values:
PassengerId    0
Survived       0
...

Saved titanic_clean.csv
```
Requirements:
- Show the before state with shape and missing value counts
- Demonstrate `dropna(subset=["Age"])` — how many rows does this lose?
- Demonstrate `fillna()` using the median for Age and the mode for Embarked
- Drop the Cabin column entirely (77% missing — not worth keeping)
- Save the cleaned DataFrame to `titanic_clean.csv` using `.to_csv(index=False)`

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — dropna vs fillna</summary>
`df.dropna(subset=["Age"])` removes rows where Age is missing. `df["Age"].fillna(value)` replaces missing Age values with `value` while keeping all rows. Use `.copy()` before modifying to avoid changing the original.
</details>

<details>
<summary>Hint 2 — Getting the mode</summary>
`df["Embarked"].mode()[0]` gives you the most common value. `mode()` returns a Series, so `[0]` grabs the first (and usually only) element.
</details>

<details>
<summary>Hint 3 — Dropping a column</summary>
`df.drop(columns=["Cabin"])` returns a new DataFrame without that column. Assign it back: `df_filled = df_filled.drop(columns=["Cabin"])`.
</details>

</details>

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
Create `pandas_groupby.py`. Produce three grouped analyses of the cleaned Titanic data. The output should look like:
```
=== Survival Analysis ===

By passenger class:
        total  survivors  survival_rate  avg_age  avg_fare
Pclass
1         216        136           0.63    38.23     84.15
2         184         87           0.47    29.88     20.66
3         491        119           0.24    25.14     13.68

Survival rate by class AND gender:
                  survivors  total  rate
Pclass Sex
1      female          91     94  0.97
       male            45    122  0.37
...

Survival by age group:
            survived  total  rate
AgeGroup
Child             35     50  0.70
Teen              14     24  0.58
...
```
Requirements:
- Use `.groupby().agg()` with a dict of aggregation functions for the class analysis
- Use multi-level groupby: `df.groupby(["Pclass", "Sex"])`
- Create an "AgeGroup" column using `pd.cut()` with bins for Child (0–12), Teen (13–18), Young Adult (19–35), Adult (36–60), Senior (61+)
- Round all rates to 2 decimal places

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Named aggregation with .agg()</summary>
`df.groupby("Pclass").agg(total=("Survived", "count"), survivors=("Survived", "sum"), ...)` — this syntax lets you name each output column. Each tuple is `(source_column, aggregation_function)`.
</details>

<details>
<summary>Hint 2 — Multi-level groupby</summary>
`df.groupby(["Pclass", "Sex"])["Survived"].agg(["sum", "count", "mean"])` groups by two columns at once, creating a multi-index. Rename the columns after: `.columns = ["survivors", "total", "rate"]`.
</details>

<details>
<summary>Hint 3 — pd.cut() for age bins</summary>
`pd.cut(df["Age"], bins=[0, 12, 18, 35, 60, 100], labels=["Child", "Teen", "Young Adult", "Adult", "Senior"])` creates a categorical column. Assign it: `df["AgeGroup"] = pd.cut(...)`.
</details>

</details>

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
- Cell 1 (Markdown): `# Titanic Survival Analysis` + a 2-sentence description of what the notebook does
- Cell 2: imports (`import pandas as pd`, `import numpy as np`)
- Cell 3: load data, `.head()`, `.info()`
- Cell 4: missing value analysis + cleaning (adapt your cleaning code from Tuesday)
- Cell 5: survival rate overall — calculate and print it
- Cell 6: survival by class — use groupby
- Cell 7: survival by gender — use groupby
- Cell 8 (Markdown): `## Key Findings` + 3 bullet points in your own words describing what you found

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
Create `notebooks/README.md`. Write it yourself based on what you actually found in your notebook — the numbers and findings should be from your own output, not copied from anywhere. Include:
- What dataset was analyzed and how many records
- 3–4 key findings with actual percentages
- What libraries were used
- Where the data came from

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
Run `pip install matplotlib` first, then create a `charts/` directory (`mkdir charts`). Create `matplotlib_intro.py`.

Build two charts and save them as PNG files. The first should be a line chart of some data points with markers, a title, axis labels, and a grid. The second should be the parabola y = x² plotted as a smooth curve from x = -3 to x = 3 with a legend. Both should be saved to the `charts/` folder.

Verify your output by opening the PNG files — they should look like polished charts, not rough sketches.

Requirements:
- Use `plt.figure(figsize=...)` to set a reasonable size
- Add title, x label, y label, and grid to the first chart
- Use `np.linspace(-3, 3, 100)` for 100 smooth x-values on the parabola
- Use `plt.savefig("charts/filename.png", dpi=150)` before `plt.show()`
- Print a confirmation message after each save

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Basic chart structure</summary>
The pattern is: `plt.figure()` → plot your data → add labels/title → `plt.savefig()` → `plt.show()`. Always save before showing — after `show()` the figure is cleared.
</details>

<details>
<summary>Hint 2 — Line chart with markers</summary>
`plt.plot(x, y, color="steelblue", linewidth=2, marker="o", markersize=6)` plots a line and puts a circle marker at each data point.
</details>

<details>
<summary>Hint 3 — The legend</summary>
Add `label="y = x²"` to your plot call, then call `plt.legend()` to display it. Without `legend()`, the label does nothing.
</details>

</details>

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
Create `charts_bar_hist.py`. Using the cleaned Titanic data, produce a single figure with two side-by-side charts and save it to `charts/bar_and_histogram.png`.

Left chart: a bar chart showing survival rate (%) for each passenger class, with the percentage labeled above each bar.

Right chart: a histogram showing the age distribution of all passengers, with a dashed vertical line marking the median age.

Both charts should have titles, axis labels, and look polished enough to include in a portfolio.

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Side-by-side subplots</summary>
`fig, axes = plt.subplots(1, 2, figsize=(12, 5))` creates one figure with two axes side by side. Use `axes[0]` and `axes[1]` instead of `plt.` for each chart.
</details>

<details>
<summary>Hint 2 — Labels above bars</summary>
After drawing bars, loop through them to add text. Each bar object has `.get_x()`, `.get_width()`, and `.get_height()` methods to find the right position.
</details>

<details>
<summary>Hint 3 — Vertical line on histogram</summary>
`axes[1].axvline(median_value, color="red", linestyle="--", linewidth=2, label=f"Median: {median_value:.0f}")` draws a dashed vertical line at the median.
</details>

</details>

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
Create `scatter_plots.py`. Using the cleaned Titanic data, produce a scatter plot of Age vs Fare where each point is colored by whether the passenger survived (green = survived, red = did not). Add a dashed trend line across the data. Save to `charts/scatter_age_fare.png`.

The chart should clearly show that survival and fare level are related, and that the trend line shows whether older passengers tended to pay more.

Requirements:
- Plot survivors and non-survivors as two separate scatter series with a legend
- Cap the y-axis at 300 to trim extreme fare outliers from view
- Add a grid with low opacity
- The trend line uses `np.polyfit()` and `np.poly1d()` to fit a line to the data — look these up if needed

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Two separate scatter series</summary>
Filter the DataFrame first: `survivors = df[df["Survived"] == 1]`. Then call `ax.scatter(survivors["Age"], survivors["Fare"], ...)` for survivors and again for non-survivors with different colors. Each call adds a separate layer.
</details>

<details>
<summary>Hint 2 — The trend line</summary>
`z = np.polyfit(x_values, y_values, 1)` fits a degree-1 polynomial (a line) and returns coefficients. `p = np.poly1d(z)` turns those into a callable function. Then `ax.plot(x_range, p(x_range))` draws the line.
</details>

<details>
<summary>Hint 3 — Handling missing values for the trend line</summary>
`np.polyfit` will crash if either array has NaN values. Create a boolean mask first: `mask = df["Age"].notna() & df["Fare"].notna()`, then use `df.loc[mask, "Age"]` and `df.loc[mask, "Fare"]` as inputs.
</details>

</details>

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

Add `import matplotlib.pyplot as plt` and `%matplotlib inline` to the imports cell at the top. Then add three new cells at the end, each containing one of this week's charts:
- Cell 9: Bar chart of survival rate by class
- Cell 10: Histogram of age distribution
- Cell 11: Scatter plot (age vs fare colored by survival)
- Cell 12 (Markdown): `## Visual Conclusions` — write 2–3 sentences in your own words interpreting what the charts show together

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
Review your charts from this week. Which four visuals tell the most complete story about the Titanic data?

**Minutes 30–50: Build a summary dashboard figure**
Create `titanic_dashboard.py`. Combine four charts into a single 2×2 figure saved as `charts/titanic_dashboard.png`. The four panels should show:
- Top left: survival rate by passenger class (bar chart)
- Top right: survival rate by gender (bar chart)
- Bottom left: age distribution split by survived vs died (overlapping histograms)
- Bottom right: fare distribution by class (box plot)

The finished figure should have an overall title, clean labels, and look like something you'd present to an audience.

Requirements:
- Use `plt.subplots(2, 2, figsize=(13, 9))`
- Each subplot should have its own title and axis labels
- The overlapping histograms need `alpha` values below 1.0 so both are visible
- Use `bbox_inches="tight"` when saving to prevent titles from getting clipped

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Accessing subplots</summary>
With `fig, axes = plt.subplots(2, 2)`, access individual panels with `axes[row, col]`: `axes[0, 0]` is top-left, `axes[1, 1]` is bottom-right.
</details>

<details>
<summary>Hint 2 — Overlapping histograms</summary>
Call `ax.hist()` twice on the same axes — once for survivors, once for non-survivors. Use `alpha=0.6` on both so they're semi-transparent and you can see both distributions.
</details>

<details>
<summary>Hint 3 — Box plot syntax</summary>
`ax.boxplot([class1_fares, class2_fares, class3_fares], labels=["1st", "2nd", "3rd"])` where each input is a Series of fare values filtered by class.
</details>

</details>

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
Create `ml_concepts.py`. Generate a synthetic dataset of 100 house sizes and prices, split it into training and test sets, and print a summary showing what each set will be used for. The output should look like:
```
Dataset: 100 houses
Size range: 812 - 3487 sq ft
Price range: $97,650 - $544,850

Training set: 80 samples
Testing set:  20 samples

The model will TRAIN on the training set.
We will EVALUATE it on the test set — data it has never seen.
This tells us how well the model generalizes to new data.
```
Requirements:
- Use `np.random.seed(42)` for reproducibility
- Generate prices as roughly `size * 150` plus some random noise (±$20,000)
- Use `train_test_split()` from scikit-learn with `test_size=0.2`
- Reshape the sizes array to 2D using `.reshape(-1, 1)` — scikit-learn requires this for single-feature input

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Generating the dataset</summary>
`np.random.randint(800, 3500, 100)` gives you 100 random house sizes. For prices: `sizes * 150 + np.random.randint(-20000, 20000, 100)`.
</details>

<details>
<summary>Hint 2 — Why reshape(-1, 1)?</summary>
scikit-learn expects input features as a 2D array (rows = samples, columns = features). A 1D array like `[800, 1200, ...]` has shape `(100,)`. Reshaping to `(-1, 1)` gives shape `(100, 1)` — 100 samples, 1 feature each.
</details>

<details>
<summary>Hint 3 — train_test_split</summary>
`X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)` — `test_size=0.2` means 20% goes to the test set. `random_state=42` makes the split reproducible.
</details>

</details>

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
Create `linear_regression.py`. Using the same house dataset from yesterday, train a linear regression model, evaluate it on the test set, print what it learned, and produce a scatter + regression line chart saved to `charts/linear_regression.png`. The output should look like:
```
Learned relationship:
  Price = 149.73 × size + 3241.18
  (True relationship is approximately: price = 150 × size)

Test set results:
  R² score: 0.971  (1.0 = perfect, 0 = random)
  RMSE: $12,847  (average prediction error)

  Predicted price for 1000 sq ft: $152,971
  Predicted price for 2000 sq ft: $302,701
  Predicted price for 3000 sq ft: $452,431
```
Requirements:
- Use `LinearRegression` from scikit-learn
- Print the learned coefficient and intercept — how close are they to the true values (150 and ~0)?
- Evaluate with `r2_score` and `mean_squared_error` (take the square root for RMSE)
- Predict prices for houses of 1000, 2000, and 3000 sq ft
- The chart shows actual test points as a scatter and the model's predictions as a line

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Training the model</summary>
`model = LinearRegression()` creates it. `model.fit(X_train, y_train)` trains it — this is where "learning" happens. After fitting, `model.coef_[0]` is the slope and `model.intercept_` is the y-intercept.
</details>

<details>
<summary>Hint 2 — RMSE from MSE</summary>
`mean_squared_error(y_test, y_pred)` gives Mean Squared Error. Wrap it in `np.sqrt()` to get Root Mean Squared Error — this is in the same units as price, making it easier to interpret.
</details>

<details>
<summary>Hint 3 — The chart</summary>
`plt.scatter(X_test, y_test)` plots actual values. `plt.plot(X_test, y_pred)` plots the model's predictions as a line. Sort X_test first if the line looks jagged: `plt.plot(sorted(X_test.flatten()), ...)`.
</details>

</details>

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
Create `classification_iris.py`. Load the built-in Iris dataset, train a K-Nearest Neighbors classifier, evaluate it, and demonstrate prediction on a new flower. The output should look like:
```
Iris dataset:
  Samples: 150
  Features: 4 (sepal length (cm), sepal width (cm), petal length (cm), petal width (cm))
  Classes: ['setosa' 'versicolor' 'virginica']

KNN (k=3) Accuracy: 100.0%

Detailed report:
              precision    recall  f1-score   support
     setosa       1.00      1.00      1.00        10
 versicolor       1.00      1.00      1.00         9
  virginica       1.00      1.00      1.00        11

New flower prediction: setosa
Probabilities: {'setosa': '100%', 'versicolor': '0%', 'virginica': '0%'}
```
Requirements:
- Use `load_iris()` from scikit-learn — no CSV needed
- Use `KNeighborsClassifier(n_neighbors=3)` 
- Evaluate with `accuracy_score` and `classification_report`
- Predict the class of a new flower with measurements `[5.1, 3.5, 1.4, 0.2]`
- Print prediction probabilities using `predict_proba()`

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Loading the Iris dataset</summary>
`from sklearn.datasets import load_iris` then `iris = load_iris()`. The features are in `iris.data`, the labels in `iris.target`, the class names in `iris.target_names`, and feature names in `iris.feature_names`.
</details>

<details>
<summary>Hint 2 — Making a single prediction</summary>
`model.predict([[5.1, 3.5, 1.4, 0.2]])` — note the double brackets. scikit-learn expects a 2D array even for a single sample. The result is an array with one element; index into it with `[0]`.
</details>

<details>
<summary>Hint 3 — predict_proba</summary>
`model.predict_proba([[5.1, 3.5, 1.4, 0.2]])[0]` gives an array of probabilities — one per class, in the same order as `iris.target_names`. Zip them together to print the class names alongside their probabilities.
</details>

</details>

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
Create `model_comparison.py`. Train three different classifiers on the same Iris data, compare their accuracy, identify the best one, and print its confusion matrix. The output should look like:
```
=== MODEL COMPARISON ===

KNN (k=3)                 Accuracy: 100.0%
Decision Tree             Accuracy: 96.7%
Logistic Regression       Accuracy: 100.0%

Best model: KNN (k=3) (100.0%)

Confusion matrix (KNN (k=3)):
Rows = Actual, Columns = Predicted
Classes: ['setosa', 'versicolor', 'virginica']
[[10  0  0]
 [ 0  9  0]
 [ 0  0 11]]
Diagonal = correct predictions, Off-diagonal = errors
```
Requirements:
- Models: `KNeighborsClassifier(n_neighbors=3)`, `DecisionTreeClassifier(max_depth=3)`, `LogisticRegression(max_iter=200)`
- Use the same train/test split for all three models so the comparison is fair
- Use `max()` with a key function to find the best model programmatically (don't hardcode it)
- Print the confusion matrix only for the best model

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Storing models in a dict</summary>
`models = {"KNN (k=3)": KNeighborsClassifier(n_neighbors=3), ...}`. Then loop: `for name, model in models.items(): model.fit(...); scores[name] = accuracy_score(...)`.
</details>

<details>
<summary>Hint 2 — Finding the best model</summary>
`best_name = max(scores, key=scores.get)` returns the key with the highest value. Then `best_model = models[best_name]` gives you the trained model object.
</details>

<details>
<summary>Hint 3 — Reading a confusion matrix</summary>
Each row is an actual class, each column is a predicted class. A perfect classifier has all values on the diagonal (top-left to bottom-right) and zeros everywhere else. Off-diagonal values are misclassifications.
</details>

</details>

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
Re-read `linear_regression.py`, `classification_iris.py`, and `model_comparison.py`. On paper or in a text file, sketch the steps of a supervised ML pipeline: Data → Split → Train → Predict → Evaluate. Write one sentence about what each step does.

**Minutes 30–50: Build a clean pipeline script**
Create `ml_pipeline_iris.py`. Rewrite the Iris classification as a clean, well-documented script where every step is its own function with a docstring. The output should be the same as before, but the code should follow this structure:

- `load_data()` — loads and returns the dataset
- `preprocess(X_train, X_test)` — applies StandardScaler (fit on train, transform both)
- `train_model(X_train, y_train)` — creates and fits a KNN model, returns it
- `evaluate(model, X_test, y_test, class_names)` — prints accuracy and classification report, returns accuracy
- `main()` — calls all four in sequence

Every function needs a one-line docstring.

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Why StandardScaler?</summary>
KNN uses distance to find neighbors. If one feature has values like 0–1 and another has values like 0–1000, the large-scale feature dominates. Scaling normalizes everything to the same range so all features contribute equally.
</details>

<details>
<summary>Hint 2 — fit_transform vs transform</summary>
`scaler.fit_transform(X_train)` learns the scale from training data AND applies it. `scaler.transform(X_test)` applies the same scale to test data WITHOUT re-learning. Never fit on test data — that would be leaking information.
</details>

<details>
<summary>Hint 3 — The main() pattern</summary>
Each function returns what the next one needs. `load_data()` returns X, y, class_names. `train_test_split()` returns the four sets. `preprocess()` returns scaled X_train and X_test. Pass each return value into the next function call.
</details>

</details>

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
Create `notebooks/titanic_ml.ipynb`. This notebook will be your ML project — build it cell by cell.

Cell 1 (Markdown): `# Titanic Survival Prediction — Machine Learning` with a 2-sentence description of what you're trying to predict and how.

Cell 2: Import pandas, numpy, scikit-learn's train_test_split and LabelEncoder, and matplotlib. Load `titanic_clean.csv` and display its shape and first few rows.

Cell 3 — Feature Engineering: ML models can't work with text like "male"/"female" — you need to convert categorical columns to numbers. Create encoded versions of the Sex and Embarked columns, then select your final feature set. Display the feature names and dataset shape.

Cell 4 — Train/Test Split: Split into 80% train and 20% test. Print the sizes of each set.

Commit at end of session:
```
git add notebooks/titanic_ml.ipynb
git commit -m "Start Titanic ML notebook: feature engineering, encoding, split"
git push
```

---

### Tuesday, Jul 29
**Theme: Train and evaluate Titanic models**

**Minutes 0–60: Continue the notebook**
Add cells that train three classifiers (Logistic Regression, Decision Tree, KNN) on the training data, evaluate each on the test set, identify the best, and display a bar chart comparing their accuracy scores. The output should show each model's accuracy percentage and which one performed best.

When you're done, every model's test accuracy should be printed, and the bar chart should make it easy to compare them visually.

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
Add a cell that trains a Decision Tree, extracts its feature importance scores, and plots them as a horizontal bar chart saved to `charts/feature_importance.png`. Sort the bars so the most important feature is at the top.

Then add a Markdown cell with your own interpretation: which feature matters most, and does that match your intuition from the EDA you did in Week 9?

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
Add a final Markdown summary cell with these sections:
- **What we did**: 4 numbered steps summarizing the ML process
- **Results**: a table showing each model and its accuracy (fill in your actual numbers)
- **Key Finding**: one paragraph describing the most important predictor and why it makes historical sense
- **What I would do next with more time**: 3 bullet points with genuine ideas

Then update `notebooks/README.md` to describe this notebook too.

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
Write it yourself — don't copy a template. It should cover: what the project does, how to run it, your actual results (real accuracy numbers from your notebook), which files do what, what skills it demonstrates, and where the data came from.

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
Write a module with a `load()` function that loads the Iris dataset using scikit-learn's built-in loader and returns it as a pandas DataFrame with columns for each feature, a numeric target column, and a human-readable species column. When run directly (`python load_data.py`), it should print the number of samples, the first few rows, and the count of each species.

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Building a DataFrame from sklearn data</summary>
`pd.DataFrame(iris.data, columns=iris.feature_names)` creates a DataFrame from the NumPy array. Then add the target column: `df["target"] = iris.target`. For the species names, use `.map({0: "setosa", 1: "versicolor", 2: "virginica"})`.
</details>

<details>
<summary>Hint 2 — Running a module directly</summary>
The `if __name__ == "__main__":` block at the bottom of the file only runs when you execute the file directly, not when it's imported. Put your test print statements there.
</details>

</details>

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

Write `src/preprocess.py` with a `split_and_scale(df)` function that:
- Separates features from target
- Performs an 80/20 stratified train/test split
- Fits a StandardScaler on the training set and applies it to both sets
- Returns X_train, X_test, y_train, y_test, and the fitted scaler

Write `src/model.py` with:
- A `MODELS` dictionary containing three classifiers: KNN (k=5), Decision Tree (max_depth=4), Logistic Regression
- A `train_all(X_train, y_train)` function that fits all models and returns a dict of trained models
- An `evaluate_all(trained_models, X_test, y_test, class_names)` function that prints accuracy and classification report for each model and returns a dict of scores

Every function needs a docstring.

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Stratified split</summary>
Add `stratify=y` to `train_test_split()`. This ensures each class is proportionally represented in both train and test sets — important when class sizes aren't equal.
</details>

<details>
<summary>Hint 2 — Returning the scaler</summary>
You need to return the fitted scaler so that `main.py` could potentially use it to scale new input data for predictions. Add it as a fifth return value.
</details>

</details>

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

Write `src/visualize.py` with a `plot_accuracy_comparison(scores, save_path)` function that creates a bar chart comparing model accuracy scores, labels each bar with its percentage, and saves the figure to the given path.

Write `main.py` at the project root that imports from all four source files and runs the complete pipeline in sequence: load → preprocess → train → evaluate → visualize → print the best model. When run with `python main.py`, the terminal should show each model's results followed by the best model and a confirmation that the chart was saved.

<details>
<summary>🆘 Stuck? Open for hints</summary>

<details>
<summary>Hint 1 — Importing from src/</summary>
At the top of main.py: `import sys; sys.path.insert(0, "src")`. Then `from load_data import load` etc. works. This is needed because Python doesn't automatically search subdirectories.
</details>

<details>
<summary>Hint 2 — Finding the best model from scores dict</summary>
`best = max(scores, key=scores.get)` returns the key (model name) with the highest value. `scores[best]` gives you its accuracy.
</details>

</details>

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
Run `python main.py` from the `projects/ml-predictor/` directory. Fix any errors until it runs cleanly end-to-end.

Then open each `.py` file and:
- Add or improve docstrings on every function that's missing one
- Add inline comments explaining any line that might not be obvious to someone reading it for the first time
- Remove any leftover debug print statements

Run it one more time. Take a screenshot of the clean terminal output.

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
Write `projects/ml-predictor/README.md` from scratch. It should tell someone who has never seen your code exactly how to run it and what to expect. Include:
- What the project does (one paragraph)
- Exact run commands
- What output to expect (terminal + saved file)
- The project structure with one-line descriptions of each file
- A results table with your actual accuracy numbers
- What skills it demonstrates
- Why this structure matters for AI coursework (hint: every ML research project uses this load → preprocess → train → evaluate pattern)

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
Open each of your three project READMEs. Check each one against this list:
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

Clone it and write your own profile README. It should include: a brief intro (who you are, what you're studying, what this summer has been about), your tech stack, a projects table linking to all three repos with descriptions, what you're currently learning, and contact info. Make it sound like you — not like a template.

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
Open a text editor (or Google Doc) and write your resume's "Projects" section. For each project, write 2 lines: one that names the project and dates, and one that describes what you built and what you achieved (use numbers — how many records, what accuracy, how many features). Then write a Technical Skills section.

Save as `resume_draft.md` in your repo's root.

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
