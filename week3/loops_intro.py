print("Counting to 10:")
i = 1
for i in range(1, 11,1):
    print("", i, end="")
    
print()
print("Even numbers 2-10:")
i = 2
for i in range(2, 21, 2):
    print("", i, end="")
print()
print("Countdown:")    
i = int(10)
for i in range(10, 0, -1):
    print("", i, end="")
    if i == 1:
        print(" Blast off!")
print()
number = int(input("Enter a number for it's time table: "))
i = 1
print(f"Times table for {number}:")
for i in range(1, 13, 1):
    print(f"{number} * {i} = ", number * i)
    
