# Write your solution here

def	ft_editor(editor):
	if editor == "word" or editor == "notepad" :
		print("awful")
	elif editor == "visual studio code":
		print("an excellent choice!")
	else:
		print("not good")

editor = ""
while editor.lower() != "visual studio code":
	editor = input("Editor: ")
	ft_editor(editor.lower())