import random

a = [random.randint(1,50) for i in range(10)]
b = [random.randint(10,80) for i in range(15)]

c = [elem_a for elem_a in a if elem_a in b]
# print(list(set(a).intersection(b))) ---> Alternative method to check for overlapping
'''
for elem_a in a:
	if elem_a in b:	
		c.append(elem_a)
'''
print("First list is " + str(a))
print("Second list is " + str(b))
print("The list with overlapping elements is " + str(c))