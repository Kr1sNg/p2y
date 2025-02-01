# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.people = []
    
    def add(self, person: Person):
        self.people.append(person)
    
    def is_empty(self):
        return (len(self.people) == 0)
    
    def print_contents(self):
        if self.is_empty() == False:
            total_height = 0
            for person in self.people:
                total_height += person.height
            print(f"There are {len(self.people)} persons in the room, and their combined height is {total_height} cm")
            for person in self.people:
                print(f"{person.name} ({person.height})")
    
    def shortest(self):
        shortist = None
        min = 250
        for person in self.people:
            if person.height < min:
                min = person.height
                shortist = person
        return shortist
    
    def remove_shortest(self):
        eliminate = self.shortest()
        if eliminate:
            self.people.remove(eliminate)
        return eliminate
        

if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()
    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    