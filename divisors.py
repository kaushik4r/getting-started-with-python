import time

num = int(input("Enter a number: "))
start_time = time.time()
divisors = range(2,num)
divisor_list = []
for elem in divisors:
	if num % elem == 0:
		#print("The number " + str(num) + " is divisble by " + str(elem))
		divisor_list.append(elem)
	'''
	else:
		print("The number " + str(num) + " isn't divisble by " + str(elem))
	'''
print(divisor_list)
print("The execution time is " + str(round(time.time() - start_time, 2)))