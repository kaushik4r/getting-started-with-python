import random

a = [random.randint(2,200) for i in range(20)]

even_list = [elem for elem in a if elem % 2 == 0]
'''
for elem in a:
	if elem % 2 == 0:
	 even_list.append(elem)
'''
print(even_list)		