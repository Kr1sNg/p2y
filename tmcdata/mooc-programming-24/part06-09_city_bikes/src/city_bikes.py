# tee ratkaisu tänne
# Write your solution here
def get_station_data(filename: str):
	stations = {}
	with open(filename) as file:
		for line in file:
			line = line.replace("\n", "")
			items = line.split(";")
			if items[0] == "Longitude":
				continue
			stations[items[3]] = (float(items[0]), float(items[1]))
	return (stations)

def distance(stations: dict, station1: str, station2: str):
	import math
	longtitude1 = stations[station1][0]
	latitude1 = stations[station1][1]
	longtitude2 = stations[station2][0]
	latitude2 = stations[station2][1]
	x_km = (longtitude1 - longtitude2) * 55.26
	y_km = (latitude1 - latitude2) * 111.2
	distance_km = math.sqrt(x_km**2 + y_km**2)
	return (distance_km)

def greatest_distance(stations: dict):
	longest = 0
	station1 = ""
	station2 = ""
	for orig in stations:
		for dest in stations:
			if distance(stations, orig, dest) > longest:
				longest = distance(stations, orig, dest)
				station1 = orig
				station2 = dest
	greatest = (station1, station2, longest)
	return (greatest)
			
# def main():
# 	s = get_station_data("stations1.csv")
# 	print(s)
# 	d = distance(s, "Designmuseo", "Hietalahdentori")
# 	print(d)
# 	d = distance(s, "Viiskulma", "Kaivopuisto")
# 	print(d)
# 	station1, station2, greatest = greatest_distance(s)
# 	print(station1, station2, greatest)

# main()