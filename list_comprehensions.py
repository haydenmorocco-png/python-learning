squares = [x * x for x in range(1,11)]
print(f"Squares: {squares}")
even_squares = [x * x for x in range(2,11,2)]
print(f"Even Squares: {even_squares}")
words = ["Hello", "World", "Python", "Is", "Great"]
uppercase_words = [word.upper() for word in words]
print(f"Uppercase: {uppercase_words}")
long_words = [word for word in words if len(word) >= 4]
print(f"Long words: {long_words}")
raw_temps = [72, -1, 68, 75, -5, 80, 71, 999, 69, 74]
valid_temps = [temp for temp in raw_temps if 0 < temp < 120]
print(f"Valid temps: {valid_temps}")
avg_temp = [f"{sum(valid_temps) / len(valid_temps):.1f}"]
print(f"Avg valid temp: {avg_temp}")
fahrenheit = [32, 68, 86, 104, 212]
cel = [f"{((f - 32) * 5/9):.1f}" for f in fahrenheit]
print(f"Celsius: {cel}")