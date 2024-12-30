# Write your solution here
stu = int(input("How many students on the course? "))
size = int(input("Desired group size? "))
group = int(round((stu + size - 1) // size))
print(f"Number of groups formed: {group}")