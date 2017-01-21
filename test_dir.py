import os

if os.path.exists('python_practice'):
	print("not creating the directory")
else:
	os.makedirs('python_practice')