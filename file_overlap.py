def overlap_list(file_name):
	return_list = []
	with open(file_name) as f:
		line = f.readline()
		while line:
			return_list.append(line)
			line = f.readline()
	return return_list
	
UB_list = overlap_list('test1.txt')
UFL_list = overlap_list('test2.txt')

check_overlap = [elem for elem in UB_list if elem in UFL_list]

print(check_overlap)