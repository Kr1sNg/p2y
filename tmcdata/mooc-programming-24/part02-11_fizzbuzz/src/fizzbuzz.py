# Write your solution here
x = int(input("Number: "))

if x % 3 == 0 and x % 5 != 0:
	print("Fizz")
elif x % 5 == 0 and x % 3 != 0 :
	print("Buzz")
elif (x % 3 == 0 and x % 5 == 0) :
	print("FizzBuzz")