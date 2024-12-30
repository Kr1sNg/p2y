# Write your solution here
def most_common_character(s: str):
	most = s[0]
	for i in s:
		if s.count(i) > s.count(most):
			most = i
	return (most)

if __name__ == "__main__":
	first_string = "abcdbde"
	print(most_common_character(first_string))

	second_string = "exemplaryelementary"
	print(most_common_character(second_string))