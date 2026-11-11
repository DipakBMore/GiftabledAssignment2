rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    # Print spaces for pyramid shape
    print("  " * (rows - i), end="")
    
    # Print numbers separated by 3 spaces
    for j in range(1, i + 1):
        print(f"{j}   ", end="")
        
    print()