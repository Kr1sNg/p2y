# Write your solution here
from datetime import datetime

def is_it_valid(pic: str) -> bool:
	if len(pic) != 11:
		return False
	control = "0123456789ABCDEFHJKLMNPRSTUVWXY"
	birthday = pic[0:2]
	birthmonth = pic[2:4]
	birthyear = pic[4:6]
	if pic[6] == "+":
		birth = f"{birthday}-{birthmonth}-18{birthyear}"
	elif pic[6] == "-":
		birth = f"{birthday}-{birthmonth}-19{birthyear}"
	elif pic[6] == "A":
		birth = f"{birthday}-{birthmonth}-20{birthyear}"
	else:
		return False
	format = '%d-%m-%Y'
	try:
		res1 = bool(datetime.strptime(birth, format))
	except ValueError:
		res1 = False
	try:
		birthnumber = int(pic[0:6] + pic[7:10]) % 31
		z_control = control[birthnumber]
		res3 = bool(z_control == pic[10])
	except ValueError:
		res3 = False
	if res1 and res3:
		return True
	else:
		return False 

if __name__ == "__main__":
	print(str(is_it_valid("080842-720N")))