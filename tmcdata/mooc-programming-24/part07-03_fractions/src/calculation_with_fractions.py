# Write your solution here
from fractions import Fraction
def fractionate(amount: int) -> list:
	result = []
	for i in range(amount):
		result.append(Fraction(1, amount))
	return (result)

if __name__ == "__main__":
	for p in fractionate(3):
		print(p)
	print()
	print(fractionate(5))
