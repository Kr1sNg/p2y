# Write your solution here

p = input("Password: ")

while True:
	r = input("Repeat password: ")
	if (r == p):
		print("User account created!")
		break
	print("They do not match!")