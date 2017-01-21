num = int(input("Enter a number: "))
check = int(input("Enter a number to check: "))

if check % num == 0:
	print(str(num) + " is evenly divided by " + str(check))
else:
	print(str(num) + " is not divided properly by " + str(check))

if num % 2 == 0:
	if num % 4 == 0:
		print("The number is even and divisible by 4")
	else:
		print("The number is even but not divisible by 4")
else:
	print("The number is odd")
print("The number is : " + str(num))