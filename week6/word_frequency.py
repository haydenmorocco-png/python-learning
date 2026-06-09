sample_text = """Artificial intelligence is transforming the world. Machine learning, 
a subset of artificial intelligence, enables computers to learn from data.
Deep learning, a subset of machine learning, uses neural networks.
Neural networks are inspired by the human brain. The human brain processes
information in parallel. Parallel processing makes neural networks powerful.
Data is the fuel for artificial intelligence. More data means better models.
Better models lead to better artificial intelligence systems."""

def clean_words(sample_text):
    clean_text = sample_text.lower().split()
    words = [word.strip('.,:;!?') for word in clean_text]
    return words

def count_words(words):
    word_count = {}
    for word in words:
        if len(word) >= 2:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    return word_count

def top_words(word_count, number):
    frequent_words = sorted(word_count.items(), key=lambda item : item[1], reverse=True)
    real_frequent_words = frequent_words[:int(number)]
    return real_frequent_words

def print_report(words, word_count, frequent_words):
    print(f"Total words: {len(words)}")
    print(f"Unique words: {len(word_count)}")
    print(f"Top {len(frequent_words)} most frequent words:")
    for i, (word, frequency) in enumerate(frequent_words, start= 1):
        print(f"{i:2}.  {word:<15}  {frequency:2} ({((frequency / len(words)) * 100):.1f}%)")
    return


words = clean_words(sample_text)
word_count = count_words(words)
frequent_words = top_words(word_count, input("How many of the top words: "))
print_report(words, word_count, frequent_words)
with open("word_freq_output.txt", "w") as f:
    for (word, freq) in frequent_words:
        f.write(f"{word:10} {freq:2} \n")

