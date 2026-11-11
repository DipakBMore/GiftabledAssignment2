#prime check

Input_num = int(input("Enter a number: "))
is_prime = True
divisable = 0
# Numbers less than or equal to 1 are not prime
if Input_num <= 1:
    is_prime = False
elif Input_num == 2:
    is_prime = True
else:	
	for i in range(2, Input_num // 2 + 1):
            if Input_num % i == 0:
                is_prime = False
                divisable = i
                break

if is_prime:
    print(f"{Input_num} is a prime number.")
else:
    print(f"{Input_num} is divisible by {divisable}\n {Input_num} is not a prime number.")