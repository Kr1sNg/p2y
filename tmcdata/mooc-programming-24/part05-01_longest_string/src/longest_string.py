# Write your solution here

def longest(strings: list) -> str:
	length = ""
	for string in strings:
		if len(string) > len(length):
			length = string
	return (length)

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))