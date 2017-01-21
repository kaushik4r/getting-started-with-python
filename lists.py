a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = [elem for elem in a if elem < 5]
'''
for elem in a:
	if elem < 5:
		new_list.append(elem)
'''
print(new_list)