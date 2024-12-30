# Write your solution here
def ft_read(path):
	recipe_book = []
	recipe = [] #[int(time), ingredient1, ing2...]
	with open(path) as file:
		for line in file:
			line = line.strip()
			if line:
				recipe.append(line)
			else:
				if recipe:
					recipe_book.append(recipe)
					recipe = []
	if recipe:
		recipe_book.append(recipe)
	return (recipe_book)
		
def search_by_name(filename: str, word: str):
	recipe_book = ft_read(filename)
	found_recipes = []
	for recipe in recipe_book:
		if word in recipe[0].lower():
			found_recipes.append(recipe[0])
	return (found_recipes)
	
def search_by_time(filename: str, prep_time: int):
	recipe_book = ft_read(filename)
	found_recipe = []
	for recipe in recipe_book:
		if int(recipe[1]) <= prep_time:
			name = recipe[0]
			tim = recipe[1]
			string = f"{name}, preparation time {tim} min"
			found_recipe.append(string)
	return (found_recipe)

def search_by_ingredient(filename: str, ingredient: str):
	recipe_book = ft_read(filename)
	found_recipes = []
	for recipe in recipe_book:
		for i in range(2, len(recipe)):
			if ingredient == recipe[i]:
				name = recipe[0]
				tim = recipe[1]
				string = f"{name}, preparation time {tim} min"
				found_recipes.append(string)
	return (found_recipes)

def main():
	found_recipes = search_by_ingredient("recipes1.txt", "eggs")

	for recipe in found_recipes:
		print(recipe)
	
main()

