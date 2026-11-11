whole_num = int(input("Enter whole number: "))
if whole_num <= 0:
    print("Number is not greater than 0, ending the program.") 

else:
tot_steps = 0
max_value = whole_num
orig_num = whole_num

# Loop until the sequence comes to 1
    while whole_num != 1:
        if whole_num % 2 == 0:  # if Even: halve it
            whole_num = whole_num // 2
        else: #if Odd, multiply by 3 and add 1
            whole_num = 3 * whole_num + 1

	if whole_num > max_value
		max_value = whole_num

	tot_steps += 1

print(f"{orig_num} reached 1 in {steps} steps")
print(f"Peak value was : {max_val}")