text = """Python is a great programming language. Python is used for 
data science, web development, and artificial intelligence. 
Python is beginner friendly and Python has a huge community. 
Many data scientists use Python every day. Artificial intelligence 
and machine learning are growing fields. Data science uses Python 
more than any other language. The Python community is very active."""
word_count = 0

low_text = text.lower().split()
words = [word.strip('.,:;!?') for word in low_text]
new_words = {}
for word in words:
    if word in new_words:
        new_words[word] += 1
    else:
        new_words[word] = 1
frequent_words = sorted(new_words.items(), key=lambda item : item[1], reverse=True)
print(f"Total words: {len(words)}")
print(f"Unique words: {len(new_words)}")
print("Top 10 most frequent words:")
for i, (word, frequency) in enumerate(frequent_words, start= 1):
    if i <= 10:
        print(f"{i:2}.  {word:<15}  {frequency:2}" , end=" ")
        t = 0
        while t < frequency:
            print("█" , end="")
            t += 1
        print()
    else:
        break
        
    