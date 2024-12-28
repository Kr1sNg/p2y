# wite your solution here
def ft_name(file):
	id_std = {}
	for line in file:
		line = line.replace("\n", "")
		names = line.split(";")
		if names[0] == "id":
			continue
		id_std[names[0]] = names[1] + " " + names[2]
	return (id_std)

def ft_exer(file):
	id_exer = {}
	for line in file:
		line = line.replace("\n", "")
		exer = line.split(";")
		if exer[0] == "id":
			continue
		sum_exer = 0
		for i in range(1, len(exer)):
			sum_exer += int(exer[i])
		id_exer[exer[0]] = sum_exer
	return (id_exer)

def ft_sum(exer_p: int, exam_p: int) -> int:
	summ = exer_p + exam_p
	if summ < 15:
		return (0)
	elif 15 <= summ <= 17:
		return (1)
	elif 18 <= summ <= 20:
		return (2)
	elif 21 <= summ <= 23:
		return (3)
	elif 24 <= summ <= 27:
		return (4)
	else:
		return (5)

def ft_point(id_exer: dict, id_exam: dict):
	id_final = {}
	for id in id_exer:
		exer_p = int(id_exer[id] * 0.25)
		if id in id_exam:
			exam_p = id_exam[id]
		id_final[id] = ft_sum(exer_p, exam_p)
	return (id_final)

def main():
	if True:
		std_info = input("Student information: ")
		exer_completed = input("Exercises completed: ")
		exam_points = input("Exam points: ")
	else:
		std_info = "students1.csv"
		exer_completed = "exercises1.csv"
		exam_points = "exam_points1.csv"
	
	with open(std_info) as file1:
		id_std = ft_name(file1)
	with open(exer_completed) as file2:
		id_exer = ft_exer(file2)
	with open(exam_points) as file3:
		id_exam = ft_exer(file3)
	id_final = ft_point(id_exer, id_exam)

	print(f'{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}')
	
	for id, name in id_std.items():
		if id in id_exer:
			exec_nbr = id_exer[id]
			exec_pts = int(id_exer[id] * 0.25)
		if id in id_exam:
			exm_pts = id_exam[id]
			tot_pts = exec_pts + exm_pts
		if id in id_final:
			grade = id_final[id]
		print(f'{name:30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{tot_pts:<10}{grade:<10}')
			
main()
