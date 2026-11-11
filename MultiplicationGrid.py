# Print multiplication grid
for row in range(1, 6):    
    for colmn in range(1, 6):
        outVar = row * colmn
        print(f"{outVar:>5d}", end="")
    print()