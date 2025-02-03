
# Write your solution here:
class Person:
    def __init__(self, name: str):
        self.__name = name
        self.__number = []
        self.__address = None
    
    def name(self):
        return self.__name
    
    def numbers(self):
        return self.__number
    
    def address(self):
        return self.__address

    def add_number(self, number: str):
        self.__number.append(number)
    
    def add_address(self, add: str):
        self.__address = add


class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if name not in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)

    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]

    def all_entries(self):
        return self.__persons
    
    def add_address(self, name: str, address: str):
        if name not in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(address)


class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)
    
    def add_address(self):
        name = input("name: ")
        add = input("address: ")
        self.__phonebook.add_address(name, add)

    def search(self):
        name = input("name: ")
        person = self.__phonebook.get_entry(name)
        if person is None:
            print("number unknown")
            print("address unknown")
            return 
        if not person.numbers():
            print("number unknown") 
        else:
            for number in person.numbers():
                print(number)
        if not person.address():
            print("address unknown")
        else:
            print(person.address())


               

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()


# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()
