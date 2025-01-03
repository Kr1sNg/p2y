# Write your solution here

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
	cheated_name = []
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
				if not ft_ontime(start_time, end_time):
					cheated_name.append(std[0])
	lst = list(set(cheated_name))
	return(lst)

if __name__ == "__main__":
	print(cheaters())