# Write your solution to exercise 1 here

i = 0
longest = 0
chars = {}

while True:
	s = input("Type in a string: ")
	if s == "":
		break
	i += 1
	if len(s) > longest:
		longest = len(s)
	for char in s:
		if char in chars:
			chars[char] += 1
		else:
			chars[char] = 1

occur = 0
most_common = ''
for char in chars:
	if chars[char] > occur:
		occur = chars[char]
		most_common = char

print(f"Total number of strings: {i}")
print(f"The length of the longest string: {longest}")
print(f"The most common character in strings: {most_common}")
	
