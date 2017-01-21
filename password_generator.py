import random
import string

''' one way for strong password '''
chars = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@!.,/#$%&*(){}[]"
pwd_length = 10
p =  "".join(random.sample(chars,pwd_length ))
#print(p)

'''better way for strong password'''
def strong_pwd(pwd_length):
	chars = string.ascii_letters + string.digits + string.punctuation
	return ''.join(random.choice(chars) for i in range(pwd_length))

'''weak password'''
def weak_pwd():
	pwd_words = "anything can be a password until and unless it is not recognizable easily".split(" ")
	return(random.choice(pwd_words))

while True:
	pwd_type = input("Do you want a strong or weak password? : ")
	if pwd_type == "strong":
		print('How many characters in your password?')
		print("This is the strongest that I could give: " + strong_pwd(int(input(""))))
		break
	elif pwd_type == "weak":
		print("This is the weak password: " + weak_pwd())
		break
	else:
		print("Give me a valid input...")
