#Digit Census.
input_num = int(input("Enter a whole number: "))

Ev_Count = 0
Odd_Count = 0
Zero_Count = 0

#if input is 0
if input_num == 0:
    Zero_Count = 1
else:
    while input_num > 0:
        iDigit = input_num % 10  # get last digit

        if iDigit == 0:			    #zero
            Zero_Count += 1
        elif iDigit % 2 == 0:		#Even
            Ev_Count += 1
        else:				        #Odd
            Odd_Count += 1
            
        input_num = input_num // 10  # Remove last digit


print(f"Even digits : {Ev_Count}")
print(f"Odd digits: {Odd_Count}")
print(f"Zero digits: {Zero_Count}")