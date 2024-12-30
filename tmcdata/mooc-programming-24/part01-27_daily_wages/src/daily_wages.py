# Write your solution here
w = float(input("Hourly wage: "))
h = float(input("Hours worked: "))
d = input("Day of the week: ")
total = float(w * h)
if d == "Sunday":
    total = total * 2
print(f"Daily wages: {total} euros")