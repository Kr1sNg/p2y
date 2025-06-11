# Write your solution here:
class Series:
	def __init__(self, name: str, nb_of_ss: int, genre: list):
		self.title = name
		self.nb_of_ss = nb_of_ss
		self.genre = genre
		self.rating = []

	
	def __str__(self):
		name = f"{self.title} ({self.nb_of_ss} seasons)\n"
		genre_str = ", ".join(self.genre)
		genres = f"genres: {genre_str}\n"
		if len(self.rating) <= 0:
			rating = f"no ratings"
		if len(self.rating) > 0:
			rating_averg = sum(self.rating) / len(self.rating)
			rating = f"{len(self.rating)} ratings, average {rating_averg:.1f} points"
		return (name + genres + rating)

	
	def rate(self, rating: int):
		if 0 <= rating <= 5:
			self.rating.append(rating)

def minimum_grade(rating: float, series_list: list):
	sries = []
	for serie in series_list:
		if len(serie.rating) > 0:
			avg = sum(serie.rating) / len(serie.rating)
		if avg >= rating:
			sries.append(serie)
	return (sries)

def includes_genre(genre: str, series_list: list):
	sries = []
	for serie in series_list:
		if genre in serie.genre:
			sries.append(serie)
	return (sries)

if __name__ == "__main__":
	dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
	print(dexter)
	dexter.rate(4)
	dexter.rate(5)
	dexter.rate(5)
	dexter.rate(3)
	dexter.rate(0)
	print(dexter)

	s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
	s1.rate(5)

	s2 = Series("South Park", 24, ["Animation", "Comedy"])
	s2.rate(3)

	s3 = Series("Friends", 10, ["Romance", "Comedy"])
	s3.rate(2)

	series_list = [s1, s2, s3]

	print("a minimum grade of 4.5:")
	for series in minimum_grade(4.5, series_list):
		print(series.title)

	print("genre Comedy:")
	for series in includes_genre("Comedy", series_list):
		print(series.title)