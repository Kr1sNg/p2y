# Write your solution here
from datetime import datetime, timedelta
book = []
file = input("Filename: ")
start = input("Starting date: ")
start_date = (datetime.strptime(start, "%d.%m.%Y"))
start_format = start_date.strftime("%d.%m.%Y")
during = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile): ")
total_min = 0
for i in range(during):
	time = start_date + timedelta(days=i)
	time_format = time.strftime('%d.%m.%Y')
	string = input(f"Screen time {time_format}: ")
	minutes = string.split(" ")
	for min in minutes:
		int_min = int(min)
		total_min += int_min
	row = f"{time_format}: {minutes[0]}/{minutes[1]}/{minutes[2]}\n"
	book.append(row)

with open(file, "w") as writenfile:
	writenfile.write(f"Time period: {start_format}-{time_format}\n")
	writenfile.write(f"Total minutes: {total_min}\n")
	writenfile.write(f"Average minutes: {total_min / during}\n")
	for line in book:
		writenfile.write(line)
	
print(f"Data stored in file {file}")
