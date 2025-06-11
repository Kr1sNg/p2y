# Write your solution here
import json

class Player:
	def __init__(self, player: str, team: str, country: str, goals: int, assists: int, games: int) -> None:
		self.player = player
		self.team = team
		self.country = country
		self.goals = goals
		self.assists = assists
		self.points = goals + assists
		self.games = games
	
	def __repr__(self):
		return f"{self.player: <21}{self.team}{self.goals: >4} + {self.assists: >2} = {self.points: >3}"

class FileProcessing:
	def __init__(self, filename: str):
		with open(filename, "r") as f:
			self.__jsondata = json.load(f)
		self.__data = []
		for player in self.__jsondata:
			self.__data.append(Player(player["name"], player["team"], player["nationality"], player["goals"], player["assists"], player["games"]))
	
	@property
	def data(self) -> list:
		return self.__data

class Search:
	def __init__(self, filename) -> None:
		stats = FileProcessing(filename)
		self.data = stats.data
	
	def total_entries(self) -> int:
		return len(self.data)
	
	def search_player(self, name: str):
		player = list(filter(lambda x: x.player == name, self.data))
		return player[0]
	
	def teams(self):
		teams_list = list(set(map(lambda x: x.team, self.data)))
		teams_list.sort()
		return teams_list
	
	def countries(self):
		countries_list = list(set(map(lambda x: x.country, self.data)))
		countries_list.sort()
		return countries_list

	def team_players(self, team: str):
		players = list(filter(lambda x: x.team == team, self.data))
		players.sort(key=lambda x: x.points, reverse=True)
		return players
	
	def country_players(self, country: str):
		players = list(filter(lambda x: x.country == country, self.data))
		players.sort(key=lambda x: x.points, reverse=True)
		return players
	
	def most_points(self):
		most_points = sorted(self.data, key=lambda x: (x.points, x.goals), reverse=True)
		return most_points
	
	def most_goals(self):
		most_goals = sorted(self.data, key=lambda x: (x.goals, -x.games), reverse=True)
		return most_goals
	
class Application:
	def __init__(self):
		pass

	def print_menu(self):
		print("commands: ")
		print("0 quit")
		print("1 search for player")
		print("2 teams")
		print("3 countries")
		print("4 players in team")
		print("5 players from country")
		print("6 most points")
		print("7 most goals")
		print()

	def execute(self):
		data = Search(input("file name: "))
		print(f"read the data of {data.total_entries()} players")
		self.print_menu()
		while True:
			cmd = int(input("command: "))
			if cmd == 0:
				break
			elif cmd == 1:
				name = input("name: ")
				print()
				print(data.search_player(name))
				print()
			elif cmd == 2:
				teams = data.teams()
				for team in teams:
					print(team)
				print()
			elif cmd == 3:
				countries = data.countries()
				for country in countries:
					print(country)
				print()
			elif cmd == 4:
				team = input("team: ")
				team_players = data.team_players(team)
				print()
				for player in team_players:
					print(player)
				print()
			elif cmd == 5:
				country = input("country: ")
				country_players = data.country_players(country)
				print()
				for player in country_players:
					print(player)
				print()
			elif cmd == 6:
				number = int(input("how many: "))
				most_point = data.most_points()
				print()
				for i in range(number):
					print(most_point[i])
				print()
			elif cmd == 7:
				number = int(input("how many: "))
				most_goals = data.most_goals()
				print()
				for i in range(number):
					print(most_goals[i])
				print()			
		print()

run = Application()
run.execute()

''' Solution:
import json
 
class Statistics:
    def __init__(self, players: list):
        self.__players = players
 
    def by_points(self,  p):
        return  p['goals'] + p['assists']
 
    def by_goals(self,  p):
        # if the numbe of goals is equal, less played games is better
        return (p['goals'], -p['games'])
 
    def player_data(self, name: str):
        for player in self.__players:
            if player['name'] == name:
                return player
 
        return None
 
    def countries(self):
        return sorted(list(set(p['nationality'] for p in self.__players )))
 
    def teams(self):
        return sorted(list(set(p['team'] for p in self.__players )))
 
    def players_in_team(self, team: str):
        players = [ p for p in self.__players if p['team'] == team]
        return sorted(players, key=self.by_points, reverse=True)
 
    def players_from_country(self, country: str):
        players = [ p for p in self.__players if p['nationality'] == country]
        return sorted(players, key=self.by_points, reverse=True)
 
    def most_points(self, countryra):
        players = sorted(self.__players, key=self.by_points, reverse=True)
        return players[0: countryra]
 
    def most_goals(self, countryra):
        players = sorted(self.__players, key=self.by_goals, reverse=True)
        return players[0: countryra]
 
class Application:
    def __init__(self):
        self.__statistics = None
 
    def instructions(self):
        instructions = """
commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals"""
        print(instructions)
 
    def f(self, p: dict):
        """
            helper method, which creates a string out of players formatted for output
        """
        points = p['goals'] + p['assists']
        return f"{p['name']:20} {p['team']}  {p['goals']:2} + {p['assists']:2} = {points:3}"
 
    def read_file(self):
        file_name = input("file: ")
        with open(file_name) as file:
            data = file.read()
 
        players = json.loads(data)
        print(f"read the data of {len(players)} players")
        self.__statistics = Statistics(players)
 
    def get_playes(self):
        name = input("name: ")
        player = self.__statistics.player_data(name)
        if player:
            print(self.f(player))
 
    def get_teams(self):
        for team in self.__statistics.teams():
            print(team)
 
    def get_countries(self):
        for country in self.__statistics.countries():
            print(country)
 
    def players_in_team(self):
        team = input("team: ")
        for player in self.__statistics.players_in_team(team):
            print(self.f(player)) 
 
    def players_from_country(self):
        country = input("country: ")
        for player in self.__statistics.players_from_country(country):
            print(self.f(player)) 
 
    def most_points(self):
        number = int(input("how many: "))
        for player in self.__statistics.most_points(number):
            print(self.f(player)) 
 
    def most_goals(self):
        number = int(input("how many: "))
        for player in self.__statistics.most_goals(number):
            print(self.f(player)) 
 
    def execute(self):
        self.read_file()
        self.instructions()
        while True:
            print()
            command = input("command: ")
            if command == "0":
                return
            elif command == "1":
                self.get_playes()
            elif command == "2":
                self.get_teams()
            elif command == "3":
                self.get_countries()
            elif command == "4":
                self.players_in_team()
            elif command == "5":
                self.players_from_country()
            elif command == "6":
                self.most_points()
            elif command == "7":
                self.most_goals()
 
Application().execute()
'''




	
