# Write your solution here
z = int(input("Year: "))
y = z
while True:
	y += 1
	if (y % 100 != 0):
		if (y % 4 == 0):
			break
	else :
		if (y % 400 == 0):
			break
print(f"The next leap year after {str(z)} is {str(y)}")

