# Write your solution here
def facto(n: int) -> int:
	if n <= 0:
		return
	if n == 1:
		return 1
	if n > 1:
		return n * facto(n - 1)

def factorials(n: int) -> dict:
	fac = {}
	for i in range(1, n + 1):
		fac[i] = facto(i)
	return fac

if __name__ == "__main__":
	k = factorials(5)
	print(k[1])
	print(k[3])
	print(k[5])