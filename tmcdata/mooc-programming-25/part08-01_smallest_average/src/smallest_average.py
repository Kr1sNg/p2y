# Write your solution here

def ft_agv_res(person: dict):
	total = 0
	for key, res in person.items():
		if key == "name":
			pass
		else:
			total += int(res)
	agv = total / (len(person) - 1)
	return (agv)

def smallest_average(person1: dict, person2: dict, person3: dict):
	a = ft_agv_res(person1)
	b = ft_agv_res(person2)
	c = ft_agv_res(person3)
	if a <= b and a <= c:
		return (person1)
	elif b < a and b <= c:
		return (person2)
	else:
		return (person3)

if __name__ == "__main__":
	person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
	person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
	person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}
	print(smallest_average(person1, person2, person3))