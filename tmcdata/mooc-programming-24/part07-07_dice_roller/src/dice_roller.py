# Write your solution here
from random import choice

def roll(die: str):
	die_a = [3, 3, 3, 3, 3, 6]
	die_b = [2, 2, 2, 5, 5, 5]
	die_c = [1, 4, 4, 4, 4, 4]
	if die == "A":
		return choice(die_a)
	elif die == "B":
		return choice(die_b)
	elif die == "C":
		return choice(die_c)
	else:
		return ("do not support")

def play(die1: str, die2: str, times: int):
	won = 0
	lose = 0
	tie = 0
	i = 0
	while i < times:
		play1 = int(roll(die1))
		play2 = int(roll(die2))
		if play1 > play2:
			won += 1
		if play1 < play2:
			lose += 1
		if play1 == play2:
			tie += 1
		i += 1
	return (won, lose, tie)
	

if __name__ == "__main__" :
	for i in range(20):
		print(roll("A"), " ", end="")
	print()
	for i in range(20):
		print(roll("B"), " ", end="")
	print()
	for i in range(20):
		print(roll("C"), " ", end="")
	print()
	result = play("A", "C", 100)
	print(result)
	result = play("A", "B", 100)
	print(result)