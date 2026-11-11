#Read a whole number from the user and print it reversed.
input_num = int(input("Enter a whole number: "))
rev_num = 0
while input_num > 0:
    # using % get the remainder
    rem = input_num % 10
    # remainder to reversed number
    rev_num = (rev_num * 10) + rem
    # Remove the last digit  
    input_num = input_num // 10


print("Reversed number:", rev_num)