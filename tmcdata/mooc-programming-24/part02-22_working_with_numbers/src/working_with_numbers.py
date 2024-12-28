# Write your solution here

print("Please type in integer numbers. Type in 0 to finish.")

i = 0
sum = 0
neg = 0
while True:
	x = int(input("Number: "))
	if x == 0:
		break
	i += 1
	sum += x
	if x < 0:
		neg += 1

print("... the program asks for numbers")
print(f"Numbers typed in {i}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {sum / i}")
print(f"Positive numbers {i - neg}")
print(f"Negative numbers {neg}")