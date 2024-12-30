# Write your solution here
# (32°F − 32) × 5/9 = 0°C

f = int(input("Please type in a temperature (F): "))
c = (f - 32) * 5/9
print(f"{f} degrees Fahrenheit equals {c} degrees Celsius")
if c < 0:
    print("Brr! It's cold in here!")