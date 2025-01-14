# Write your solution to exercise 3 here

def read_points():
	result = []
	with open("statistics.txt") as readfile:
		for line in readfile:
			line = line.replace("\n", "")
			parts = line.split(":")
			name = parts[0]
			points = (parts[1]).split("-")
			try:
				win = int(points[0])
				lose = int(points[1])
				tie = int(points[2])
				total_point = win * 3 + lose * 0 + tie * 1
			except ValueError:
				return (print(f"ValueError: Invalid format in the file: {line}"))
			result.append((name, total_point))
		return result

if __name__ == "__main__":
	res = read_points()
	print(res)

