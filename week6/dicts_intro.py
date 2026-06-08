
student_profile = {
    "name" : "Jordan Smith",
    "age"  : 20,
    "major" : "Computer Science",
    "GPA"    : 3.6,
    "is_student" : True
}

print(f"Name : {student_profile['name']}")
print(f"GPA : {student_profile['GPA']}")
print(f"Keys: {list(student_profile.keys())}")
print(f"Values: {list(student_profile.values())}")
print(f"Minor : {student_profile.get('minor', 'Undeclared')}")
student_profile["minor"] = "AI"
student_profile["GPA"] = 3.7
print(f"Updated person: {student_profile}")
print("All info:")
for (key, value) in student_profile.items():
    print(f"{key} : {value}")
    
courses = {
    "CS101": ["Alice", "Bob", "Charlie"],
    "MATH201": ["Alice", "Diana", "Eve"],
    "AI301": ["Bob", "Charlie", "Diana", "Frank"]
}

print(f"AI301 students: {list(courses["AI301"])}")
print(f"Number of AI301 students: {len(list(courses["AI301"]))}")
alice_courses = [course for course in courses if "Alice" in courses[course]]
print(f"Alice's courses: {alice_courses}")

'''
AI301 students: ['Bob', 'Charlie', 'Diana', 'Frank']
Number of AI301 students: 4
Alice's courses: ['CS101', 'MATH201']
```
Requirements:
- Use `.get("minor", "Undeclared")` for the safe access line — do not use `person["minor"]` directly
- Add a "minor" key and update the GPA after creating the dict
- Iterate using `.items()` to print all key-value pairs
- The `alice_courses` list must be built with a list comprehension, not a regular loop
'''