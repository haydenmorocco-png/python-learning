colors = {"red", "blue", "green", "red", "blue"}
print(f"Color set: {colors}")
print(f"Number of unique colors: {len(colors)}")
python_class = {'Alice', 'Charlie', 'Bob', 'Diana', 'Eve'}
java_class = {'Frank', 'Grace', 'Bob', 'Diana', 'Eve'}
all_students = python_class | java_class
print(f"Students in either course: {all_students}")
both_classes = python_class & java_class
print(f"Students in both courses: {both_classes}")
python_only = python_class - java_class
print(f"Python only: {python_only}")
raw_tags = ['python', 'AI', 'python', 'machine learning', 'AI', 'python', 'data']
print(f"Raw tags: {raw_tags}")
tag_list = {word for word in raw_tags}
new_tags = sorted(tag_list)
print(f"Unique tags: {new_tags}")
usernames = ["alice_j", "hacker_x", "bob_k", 'unknown_user']
valid_usernames = {"alice_j", "bob_k"}
for name in usernames:
    if name in valid_usernames:
        print(f'{name}: Valid')
    else:
        print(f'{name}: Invalid')