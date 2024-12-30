# Write your solution here

cafeteria = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
groceries = float(input("How much money do you spend on groceries in a week? "))

print("Average food expenditure: ")
print(f"Daily: {(cafeteria * price + groceries) / 7} euros")
print(f"Weekly: {cafeteria * price + groceries} euros")