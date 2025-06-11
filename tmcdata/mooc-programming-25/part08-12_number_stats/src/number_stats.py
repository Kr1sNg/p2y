# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count_added = 0
        self.sum = 0
        self.even = 0
        self.even_sum = 0
        self.odd = 0
        self.odd_sum = 0

    def add_number(self, number:int):
        self.count_added += 1
        self.sum += number
        if number % 2 == 0:
            self.even += 1
            self.even_sum += number
        else:
            self.odd += 1
            self.odd_sum += number
        pass

    def count_numbers(self):
        return self.count_added
    
    def get_sum(self):
        return self.sum
    
    def average(self):
        if self.count_added != 0:
            return (self.sum / self.count_added)



def main():
    print("Please type in integer numbers: ")
    stats = NumberStats()
    while True:
        try:
            number = int(input())
            if number == -1:
                break
        except ValueError:
            return
        stats.add_number(number)
    print(f"Sum of numbers: {stats.get_sum()}")
    print(f"Mean of numbers: {stats.average()}")
    print(f"Sum of even numbers: {stats.even_sum}")
    print(f"Sum of odd numbers: {stats.odd_sum}")

main()

