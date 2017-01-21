import datetime
now = datetime.datetime.now()
name = input("Enter your name: ")
age = int(input("Enter your age: "))
new_age = (now.year - age) + 100
print( name + "'s age after 100 years will be: " + str(new_age))
