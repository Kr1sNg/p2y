# WRITE YOUR SOLUTION HERE:

class WeatherStation:
	def __init__(self, station: str):
		if station == "":
			raise ValueError("Put the name")
		else:
			self.__name = station
			self.__observ = []
	
	# @property
	# def name(self):
	# 	return self.__name

	def add_observation(self, observation: str):
		if observation == "":
			raise ValueError("empty")
		else:
			self.__observ.append(observation)
	
	def latest_observation(self):
		leng = len(self.__observ)
		if leng <= 0:
			return ""
		else:
			return self.__observ[leng - 1]
	
	def number_of_observations(self):
		return (len(self.__observ))
	
	def __str__(self):
		return f"{self.__name}, {len(self.__observ)} observations" 

if __name__ == "__main__":
	station = WeatherStation("Houston")
	station.add_observation("Rain 10mm")
	station.add_observation("Sunny")
	print(station.latest_observation())
	station.name = "Hi"
	print(station)
