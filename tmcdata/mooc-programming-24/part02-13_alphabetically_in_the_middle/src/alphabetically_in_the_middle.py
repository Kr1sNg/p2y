# Write your solution here
a = input("1st letter: ")
b = input("2nd letter: ")
c = input("3rd letter: ")

if (a >= b and a >= c) :
	if (b >= c) :
		print(f"The letter in the middle is {b}")
	else :
		print(f"The letter in the middle is {c}")
elif (a < b and a < c):
	if (b <= c) :
		print(f"The letter in the middle is {b}")
	else :
		print(f"The letter in the middle is {c}")
else:
	print(f"The letter in the middle is {a}")
