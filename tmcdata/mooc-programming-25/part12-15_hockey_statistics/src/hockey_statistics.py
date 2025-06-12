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






	
