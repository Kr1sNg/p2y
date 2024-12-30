# Write your solution here
i = int(input("How many points [0-100]: "))

if i < 0 or i > 100:
	print("Grade: impossible!")
elif 0 <= i <= 49:
	print("Grade: fail")
elif 50 <= i <= 59:
	print("Grade: 1")
elif 60 <= i <= 69:
	print("Grade: 2")
elif 70 <= i <= 79:
	print("Grade: 3")
elif 80 <= i <= 89:
	print("Grade: 4")
else:
	print("Grade: 5")