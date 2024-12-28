# write your solution here
if True:
	student_info = input("Student information: ")
	exercise_data = input("Exercises completed: ")
else:
	student_info = "students1.csv"
	exercise_data = "exercises1.csv"
# {'std': (1, 2, 3), 'std2' = (4, 5, 6)}
id_std = {} 
with open(student_info) as file:
	for line in file:
		line = line.replace("\n", "")
		names = line.split(';') #[[id0, name0, last0], [id1, name1, last1]]
		if names[0] == "id":
			continue
		id_std[names[0]] = names[1] + " " + names[2]

id_grd = {}
with open(exercise_data) as file:
	for line in file:
		line = line.replace('\n', '')
		grades = line.split(';') #[[id0, gr0, gr1, gr2]]
		if grades[0] == "id":
			continue
		total = 0
		for i in range(1, len(grades)):
			total += int(grades[i])
		id_grd[grades[0]] = total

for id, name in id_std.items():
	if id in id_grd:
		total_grd = id_grd[id]
		print(f"{name} {total_grd}")



