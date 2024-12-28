# Write your solution here
def histogram(s: str):
	dct = {}
	for c in s:
		if c not in dct:
			dct[c] = 1
		else:
			dct[c] += 1
	for c, occur in dct.items():
		print(f"{c} {occur * '*'}")

		
if __name__ == "__main__":
	histogram("abba")
	print()
	histogram("statistically")