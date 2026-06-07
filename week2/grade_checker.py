score = int(input("Enter your exam score (0-100):"))

print(f"Score: {score}/100")

if score >= 90:
    print("Grade: A")
    print("Feedback: Excellent work!")
elif score >= 80:
    print("Grade: B")
    print("Feedback: Good job!")
elif score >= 70:
    print("Grade: C")
    print("Feedback: Passing, but room to improve.")
elif score >= 60:
    print("Grade: D")
    print("Feedback: At risk, Consider getting a tutor.")
else:
    print("Grade: F")
    print("Feedback: Did not pass. Let's talk about next steps.")