# dic[key] = value => dic[value] = key
# Write your solution here
def invert(dictionary: dict):
	new = {}
	for key in dictionary:
		value = dictionary[key]
		new[value] = key
	for value in new:
		dictionary[value] = new[value]
		dictionary.pop(new[value])
	new.clear()


if __name__ == "__main__":
	s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
	invert(s)
	print(s)
	
	