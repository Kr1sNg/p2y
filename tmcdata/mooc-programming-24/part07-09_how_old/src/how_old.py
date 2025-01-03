# Write your solution here
from datetime import datetime
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
millennium = datetime(1999, 12, 31, 23, 59, 59)
old = datetime(year, month, day)
age = millennium - old
if old > millennium:
	print("You weren't born yet on the eve of the new millennium.")
else:
	print(f"You were {age.days} days old on the eve of the new millennium.")