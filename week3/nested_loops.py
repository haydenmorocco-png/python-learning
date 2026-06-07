print("Multiplication Table (1-5):")
i = 1
print("      1     2     3     4     5")
print("--------------------")
for i in range(1, 6):
    print(f"{i:2}", end=" ")
    for j in range(1, 6):
        print(f"{i * j:4}", end="  ")
    print()
rows = int(input("How tall are the triangles: "))
i = 1
j = 1
for i in range(1, (rows + 1), 1):
    while j <= i:
        print("*", end="")
        j += 1
    j = 1
    i += 1
    print()
i = 1
j = 1
for i in range(1, (rows + 1), 1):
    while j <= i:
        print(j, " ", end="")
        j += 1
    j = 1
    i += 1
    print()
