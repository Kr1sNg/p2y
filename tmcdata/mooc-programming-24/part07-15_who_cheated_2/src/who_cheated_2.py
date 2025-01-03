# Write your solution here
# return dict = {'std': total_point, }

from datetime import datetime, timedelta
import csv

def ft_ontime(start: str, end: str):
	time_start = datetime.strptime(start, "%H:%M")
	time_end = datetime.strptime(end, "%H:%M")
	deadline = timedelta(hours=3)
	if time_end - time_start > deadline:
		return False
	else:
		return True

def cheaters():
	valid_submit = []
	starting = []
	submissions = []
	with open("start_times.csv") as file:
		for line in csv.reader(file, delimiter=";"):
			starting.append(line)
	with open("submissions.csv") as cheated:
		for line in csv.reader(cheated, delimiter=";"):
			submissions.append(line)
	for std in starting:
		start_time = std[1]
		for submit in submissions:
			if submit[0] == std[0]:
				end_time = submit[3]
				if ft_ontime(start_time, end_time):
					valid_submit.append(submit)
	return(valid_submit)

def book_of_tasks():
	book = {}
	valid_submit = cheaters()
	for row in valid_submit:
		if row[0] in book:
			if row[1] in book[row[0]]:
				if row[2] > book[row[0]][row[1]]:
					book[row[0]][row[1]] = row[2]
			else:
					book[row[0]][row[1]] = row[2]
		else:
			book[row[0]] = {}
			book[row[0]][row[1]] = row[2]
	return (book)

def final_points():
	book = book_of_tasks()
	std_point = {}
	for std in book:
		std_point[std] = 0
		for task in book[std]:
			std_point[std] += int(book[std][task])
	return std_point

if __name__ == "__main__":
	print(final_points())