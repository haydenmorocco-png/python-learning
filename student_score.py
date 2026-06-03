student_score = {
    'Charlie'   : 62,
    'Grace'     : 91,
    'Alice'     : 72,
    'Eve'       : 83,
    'Frank'     : 79,
    'Bob'       : 88,
    'Henry'     : 68,
    'Diana'     : 95}

sorted_scores = sorted(student_score.items(), key=lambda item : item[1], reverse=True)
for i, (name, score) in enumerate(sorted_scores):
    if score >= 90:
        print(f"{i + 1} {name} {score}   (A)")
    elif score >= 80:
        print(f"{i + 1} {name} {score}   (B)")
    elif score >= 70:
        print(f"{i + 1} {name} {score}   (C)")
    else:
        print(f"{i + 1} {name} {score}   (D/f)")
print(f"Lowest: {min(student_score.values())} Highest: {max(student_score.values())}")
avg = sum(student_score.values()) / len(student_score)
print(f"Average: {avg}")
print("Above average:", end=" ")
for (name, score) in sorted_scores:
    if score > avg:
       print(f"{name}" ,end=" ")

