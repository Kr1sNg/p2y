# Write your solution here

def ft_input():
	lst = []
	while True:
		a = input("Exam points and exercises completed: ")
		if a == "":
			break
		else:
			lst.append(a)
	return lst

def first_word(s):
    i = 0
    while (s[i] != " "):
        i += 1
    return (s[0:i])

def ft_exam(s):
	exam = int(first_word(s))
	return (exam)

def last_word(s):
    i = -1
    while (s[i] != " "):
        i -= 1
    i += 1
    return (s[i:])

def ft_exer(s):
	exer = int(last_word(s))
	return (exer)

def rounddown(i):
	if i < 10:
		return (0)
	elif 10 <= i < 20:
		return (1)
	elif 20 <= i < 30:
		return (2)
	elif 30 <= i < 40:
		return (3)
	elif 40 <= i < 50:
		return (4)
	elif 50 <= i < 60:
		return (5)
	elif 60 <= i < 70:
		return (6)
	elif 70 <= i < 80:
		return (7)
	elif 80 <= i < 90:
		return (8)
	elif 90 <= i < 100:
		return (9)
	elif i >= 100:
		return (10)

def ft_point(exam, exer):
	point = exam + rounddown(exer)
	return (point)

def ft_average(lst: list):
	total = 0
	for point in lst:
		total += point
	return (total / len(lst))
	
# def print_point(lst: list):
# 	for item in lst:
# 		print(f"{>2:}")



def main():
	lst = ft_input()
	lst_point = []
	pass_count = 0
	zero = 0
	one = 0
	two = 0
	three = 0
	four = 0
	five = 0
	for item in lst:
		exam = ft_exam(item)
		exer = ft_exer(item)
		point = ft_point(exam, exer)
		lst_point.append(point)

		if (exam < 10 or point < 15):
			zero += 1
		else:
			pass_count += 1
			if 15 <= point <= 17:
				one += 1
			elif 18 <= point <= 20:
				two += 1
			elif 21 <= point <= 23:
				three += 1
			elif 24 <= point <= 27:
				four += 1
			elif 28 <= point <= 30:
				five += 1	

	print("Statistics:")
	print(f"Points average: {ft_average(lst_point)}")
	print(f"Pass percentage: {((pass_count * 100/len(lst))):.1f}")
	print("Grade distribution:")
	print(f"  5: {five * '*'}")
	print(f"  4: {four * '*'}")
	print(f"  3: {three * '*'}")
	print(f"  2: {two * '*'}")
	print(f"  1: {one * '*'}")
	print(f"  0: {zero * '*'}")

main()

