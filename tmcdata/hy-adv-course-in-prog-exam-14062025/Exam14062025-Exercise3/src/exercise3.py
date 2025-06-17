# Write your solution to exercise 3 here

from random import randint

class Dice:
	def __init__(self, sides = 6):
		self.__num_sides = sides
	
	def roll_dice(self, times: int):
		results = []
		for i in range(times):
			results.append(randint(1, self.__num_sides))
		return results
	
	def __str__(self):
		return (f"{self.__num_sides}-sided dice")

class DiceGame:
	def __init__(self, dice: Dice):
		self.__dice = dice
	
	def roll_once(self):
		results = self.__dice.roll_dice(5)
		results.sort()
		
		if len(set(results)) == 1:
			print("Yatzy!")
		else:
			s = ", ".join(map(str, results))
			print(f"Rolled 5 dice and got {s}.")
	
	def roll_five_of_a_kind(self):
		count = 0
		while True:
			results = self.__dice.roll_dice(5)
			count += 1
			if len(set(results)) == 1:
				break
		print(f"It took {count} rolls to get five of a kind.")

	
	def __str__(self):
		return f"The goal of the game is to roll the dice and get 5 of the same number. Using {self.__dice}."


if __name__ == "__main__":

	six_sided_dice = Dice()
	game = DiceGame(six_sided_dice)

	print(game)

	game.roll_once()
	game.roll_once()
	game.roll_once()
	game.roll_once()

	game.roll_five_of_a_kind()

	difficult_game = DiceGame(Dice(10))
	difficult_game.roll_five_of_a_kind()

	easy_game = DiceGame(Dice(1))
	easy_game.roll_once()
	easy_game.roll_once()
	easy_game.roll_once()
	easy_game.roll_once()