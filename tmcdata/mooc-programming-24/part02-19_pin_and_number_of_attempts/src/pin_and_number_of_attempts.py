# Write your solution here
count = 0
while True:
	x = input("PIN: ")
	count += 1
	if (x != "4321"):
		print("Wrong")
	else:
		if count == 1:
			print("Correct! It only took you one single attempt!")
		else:
			print("Correct! It took you " + str(count) +" attempts")
		break 