

class Programs:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name.title()

    @property
    def likes(self):
        return self._likes

    def give_likes(self):
        self._likes += 1

    def __str__(self):
        return f'\n— {self._name} \n— {self.year} \n— {self._likes} Likes'


class Films(Programs):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'\n— {self._name} \n— {self.duration} Minutes \n— {self.year} \n— {self._likes} Likes'


class Series(Programs):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'\n— {self._name} \n— {self.seasons} Seasons \n— {self.year} \n— {self._likes} Likes'


class Playlist():
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    def __getitem__(self, item):
        return self._programs[item]

    @property
    def listing(self):
        return self._programs

    def __len__(self):
        return len(self._programs)


avengers = Films("avengers: infinity war", 2018, 160)
scarymovie = Films("scary movie", 1999, 100)
atlanta = Series("atlanta", 2018, 2)
daredevil = Series("daredevil", 2016, 2)

avengers.give_likes()
atlanta.give_likes()
scarymovie.give_likes()
daredevil.give_likes()

films_and_series = [avengers, atlanta, scarymovie, daredevil]
weekend_playlist = Playlist("Weekend", films_and_series)

print(f'\nPlaylist size: {len(weekend_playlist)}')
print(avengers in weekend_playlist)

for program in weekend_playlist:
    print(program)