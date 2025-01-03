# Write your solution here
from random import shuffle

def lottery_numbers(amount: int, lower: int, upper: int):
	number_pool = list(range(lower, upper + 1))
	shuffle(number_pool)
	weekly_draw = number_pool[0:amount]
	weekly_draw.sort()
	return (weekly_draw)

if __name__ == "__main__":
	for number in lottery_numbers(7, 1, 40):
		print(number)