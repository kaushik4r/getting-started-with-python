import random

#a = []
print("outside!!")
if __name__ == '__main__':
	print("in main!!")
	random_list = [random.randint(1,10) for i in range(5)]
	list_ends(random_list)
	print(a)

def list_ends(list):
	print("in list_ends")

	a.append(list[0]) 
	a.append(list[-1])
	return a