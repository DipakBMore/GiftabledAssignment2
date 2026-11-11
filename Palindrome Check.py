#Palindrome Check.
input_num = int(input("Enter a whole number: "))
Orig_num = input_num
rev_num = 0
# Reverse the number
while input_num > 0:
    # using % get the remainder
    rem = input_num % 10
    # remainder to reversed number
    rev_num = (rev_num * 10) + rem
    # Remove the last digit  
    input_num = input_num // 10

# Compare reversed number and the original

if Orig_num == rev_num:
   print(f"{Orig_num} is a palindrome number.")
else:
    print(f"{Orig_num} is not a palindrome number.")