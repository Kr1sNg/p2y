# Write your solution here
def list_sum(la, lb):
	sum = []
	if len(la) != len(lb):
		return
	for i in range(len(la)):
		sum.append(la[i] + lb[i])
	return (sum)

if __name__ == "__main__":
	a = [1, 2, 3]
	b = [7, 8, 9]
	print(list_sum(a, b))