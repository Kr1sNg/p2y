# Write your solution here
def oldest_person(people: list) -> str:
	min_year = 2024
	oldest_per = ""
	for person in people:
		if person[1] < min_year:
			min_year = person[1]
			oldest_per = person[0]
	return oldest_per

if __name__ == "__main__":
	p1 = ("Adam", 1977)
	p2 = ("Ellen", 1985)
	p3 = ("Mary", 1953)
	p4 = ("Ernest", 1997)
	people = [p1, p2, p3, p4]

	print(oldest_person(people))


		