def greeting():
    print("Hello! Welcome to Python.")
    
def greeting_personal(name):
    print(f"Hello, {name}! Welcome to Python.")
    
def addition(number_1, number_2):
    result = number_1 + number_2
    return result
    
def celsius_to_fahrenheit(celsius):
    fahr = ((9/5) * celsius) + 32
    return fahr

def fahrenheit_to_celsius(fahr):
    cel = (5/9) * (fahr - 32)
    return cel

def describe_temp(celsius):
    fahr = celsius_to_fahrenheit(celsius)
    if fahr >= 80:
        temp = "Hot"
    elif fahr >= 60:
        temp = "Comfortable"
    elif fahr >= 40:
        temp = "Cold"
    elif fahr < 40:
        temp = "Freezing"
    info = f"{celsius}°C ({fahr}°F) - {temp}"
    return info    

greeting()
greeting_personal("Hayden")
result = addition(5,7)
print(result)
celsius_to_fahrenheit(100)
fahrenheit_to_celsius(98.6)

for t in [-10, 5, 20, 35]:
    info = describe_temp(t)
    print(info)