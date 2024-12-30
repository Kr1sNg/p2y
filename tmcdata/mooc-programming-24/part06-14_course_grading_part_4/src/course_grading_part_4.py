# tee ratkaisu tänne

# wite your solution here
def ft_name(file):
	id_std = {}
	for line in file:
		line = line.strip()
		names = line.split(";")
		if names[0] == "id":
			continue
		id_std[names[0]] = names[1] + " " + names[2]
	return (id_std)

def ft_exer(file):
	id_exer = {}
	for line in file:
		line = line.strip()
		exer = line.split(";")
		if exer[0] == "id":
			continue
		sum_exer = 0
		for exe in exer[1 : ]:
			sum_exer += int(exe)
		id_exer[exer[0]] = sum_exer
	return (id_exer)

def ft_sum(exer_p: int, exam_p: int) -> int:
	summ = exer_p + exam_p
	if summ < 15:
		return (0)
	elif summ <= 17:
		return (1)
	elif summ <= 20:
		return (2)
	elif summ <= 23:
		return (3)
	elif summ <= 27:
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

def ft_header(filename: str) -> str:
	head = []
	with open(filename) as file:
		for line in file:
			head_lst = line.split(":")
			head.append(head_lst[1].strip())
	header = f"{head[0]}, {head[1]} credits"
	equal = f"{'=' * len(header)}"
	return (header + "\n" + equal + "\n")

def main():
	if True:
		std_info = input("Student information: ")
		exer_completed = input("Exercises completed: ")
		exam_points = input("Exam points: ")
		cours_info = input("Course information: ")
	else:
		std_info = "students1.csv"
		exer_completed = "exercises1.csv"
		exam_points = "exam_points1.csv"
		cours_info = "course1.txt"
	
	with open(std_info) as file1:
		id_std = ft_name(file1)
	with open(exer_completed) as file2:
		id_exer = ft_exer(file2)
	with open(exam_points) as file3:
		id_exam = ft_exer(file3)
	id_final = ft_point(id_exer, id_exam)

	s = ""
	csv = []
	for id, name in id_std.items():
		if id in id_exer:
			exec_nbr = id_exer[id]
			exec_pts = int(id_exer[id] * 0.25)
		if id in id_exam:
			exm_pts = id_exam[id]
			tot_pts = exec_pts + exm_pts
		if id in id_final:
			grade = id_final[id]
		s += f'{name:30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{tot_pts:<10}{grade:<10}\n'
		csv.append((id, name, grade)) 

	with open("results.txt", "w") as file_txt:
		file_txt.write(ft_header(cours_info))
		file_txt.write(f'{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}\n')
		file_txt.write(s)
	
	with open("results.csv", "w") as file_csv:
		for row in csv:
			file_csv.write(f"{row[0]};{row[1]};{row[2]}\n")

main()
