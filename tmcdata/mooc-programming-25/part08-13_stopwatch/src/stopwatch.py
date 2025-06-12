# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

#to print Class we need this method __str__
    def __str__(self):
        return (f"{self.minutes:02d}:{self.seconds:02d}")
        
    def tick(self):
        if 0 <= self.seconds < 59:
            self.seconds += 1
        elif self.seconds == 59:
            self.seconds = 0
            if 0 <=self.minutes < 59:
                self.minutes += 1
            elif self.minutes == 59:
                self.minutes = 0


if __name__ == "__main__":
    watch = Stopwatch()
    for i in range(3606):
        print(watch)
        watch.tick()
