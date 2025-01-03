# Write your solution here
import json

def print_persons(filename: str):
	with open(filename) as file:
		data = file.read()
	
	students = json.loads(data)
	for std in students:
		hobbs = ', '.join(std["hobbies"])
		print(f'{std["name"]} {std["age"]} years ({hobbs})')

if __name__ == "__main__":
	print_persons("file1.json")