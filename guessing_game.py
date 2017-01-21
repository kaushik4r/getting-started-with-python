import random

num = random.randint(1,9)
# print(num)
count = 0

while True:
	
	guess = int(input("Enter a guessing number between 1 and 9(inclusive): "))
	
	if num == guess:
		print("You won!!")
		count+=1
		break
		
	elif guess < num:
		print("Guess higher.. ")
		
	else:
		print("Guess lower..")
		
	count+=1

print("You made " + str(count) + " guesses.")