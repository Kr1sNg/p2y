# Write your solution here
def is_prime(number: int):
	if number < 2:
		return False
	for i in range(2, number):
		if number % i == 0:
			return False
	return True

def prime_numbers():
	i = 1
	while True:
		if is_prime(i):
			yield i
		i += 1

if __name__ == "__main__":
	numbers = prime_numbers()
	for i in range(13):
		print(next(numbers))

