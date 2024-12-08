from math import sqrt
# Write your solution here

while True:
	x = int(input("Please type in a number: "))
	if x > 0:
		print(sqrt(x))
	elif x < 0:
		print("Invalid number")
	else:
		break

print("Exiting...")