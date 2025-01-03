# Write your solution here
def change_case(orig_string: str) -> str:
	new_str = ""
	for char in orig_string:
		if char.islower():
			new_str += char.upper()
		elif char.isupper():
			new_str += char.lower()
		else:
			new_str += char
	return (new_str)

def split_in_half(orig_string: str) -> tuple:
	length = len(orig_string)
	index = (length // 2)
	new_str1 = orig_string[:index]
	new_str2 = orig_string[index:]
	return (new_str1, new_str2)

def remove_special_characters(orig_string: str) -> str:
	from string import punctuation, printable
	new_str = ""
	for char in orig_string:
		if char in punctuation or char not in printable :
			pass
		else:
			new_str += char
	return (new_str)

if __name__ == "__main__":
	print(change_case("this is UPPERCASE"))
	print(split_in_half("abc"))
	print(remove_special_characters("Thi§ is a test: test?"))