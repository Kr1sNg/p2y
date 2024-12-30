# Write your solution here

m = int(input("Value of gift: "))

if (m < 5000):
	tax = 0
elif (5000 <= m < 25000):
	tax = (100 + (m - 5000) * 0.08)
elif (25000 <= m < 55000):
	tax = (1700 + (m - 25000) * 0.1)
elif (55000 <= m < 200000):
	tax = (4700 + (m - 55000) * 0.12)
elif (200000 <= m < 1000000):
	tax = (22100 + (m - 200000) * 0.15)
else:
	tax = (142100 + (m - 1000000) * 0.17)

if (tax <= 0):
	print("No tax!")
else:
	print(f"Amount of tax: {tax} euros")