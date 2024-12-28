# write your solution here
def read_fruits():
	market_dict = {}
	with open("fruits.csv") as new_file:
		for line in new_file:
			texts = line.split(";")
			market_dict[texts[0]] = float(texts[1])
	return (market_dict)

if __name__ == "__main__":
	d = read_fruits()
	print(d)


